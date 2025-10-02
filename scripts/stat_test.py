"""
Statistical comparison of Python execution methods across benchmarks.

Requirements:
    pip install pandas scipy statsmodels numpy
"""

import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.anova import AnovaRM
from statsmodels.stats.multitest import multipletests
import itertools
import warnings

warnings.filterwarnings("ignore")

# ---------------- Config ----------------
INPUT_CSV = "..\\data\\collection_1\\combine\\greenscore_raw_per_benchmark.csv"
METHOD_COL = "method"
BENCH_COL = "benchmark"
METRICS = ["energy_j", "time_s", "carbon_g"]   # adjust if needed
ALPHA = 0.05
N_BOOT = 5000

# ---------------- Helpers ----------------
def paired_cohens_d(x, y):
    """Cohen's d for paired samples"""
    diff = np.array(x) - np.array(y)
    return diff.mean() / diff.std(ddof=1)

def bootstrap_mean_diff_ci(x, y, n_boot=5000, alpha=0.05, seed=0):
    """Bootstrap CI for mean difference (x - y)"""
    rng = np.random.default_rng(seed)
    diffs = np.array(x) - np.array(y)
    n = len(diffs)
    boot_means = []
    for _ in range(n_boot):
        sample = rng.choice(diffs, size=n, replace=True)
        boot_means.append(sample.mean())
    lower = np.percentile(boot_means, 100 * (alpha/2))
    upper = np.percentile(boot_means, 100 * (1 - alpha/2))
    return lower, upper

# ---------------- Load Data ----------------
df = pd.read_csv(INPUT_CSV)

methods = df[METHOD_COL].unique()
benchmarks = df[BENCH_COL].unique()
print(f"Found {len(methods)} methods: {methods}")
print(f"Found {len(benchmarks)} benchmarks")

anova_summary_rows = []
posthoc_rows = []

# ---------------- Run tests ----------------
for metric in METRICS:
    print(f"\n=== Metric: {metric} ===")
    pivot = df.pivot_table(index=BENCH_COL, columns=METHOD_COL, values=metric)
    pivot = pivot.dropna(axis=0)  # drop incomplete rows
    n_subjects = len(pivot)
    print(f"Using {n_subjects} benchmarks")

    # ----- Repeated measures ANOVA -----
    long = pivot.reset_index().melt(id_vars=BENCH_COL, value_name=metric, var_name=METHOD_COL)
    try:
        aov = AnovaRM(long, depvar=metric, subject=BENCH_COL, within=[METHOD_COL]).fit()
        F_val = float(aov.anova_table.loc[METHOD_COL, 'F Value'])
        p_val = float(aov.anova_table.loc[METHOD_COL, 'Pr > F'])
    except Exception as e:
        print("ANOVA failed:", e)
        F_val, p_val = np.nan, np.nan

    # ----- Friedman Test -----
    try:
        method_order = list(pivot.columns)
        args = [pivot[m].values for m in method_order]
        fried_stat, fried_p = stats.friedmanchisquare(*args)
    except Exception as e:
        fried_stat, fried_p = np.nan, np.nan

    print(f"ANOVA: F = {F_val:.5f}, p = {p_val:.5f}")
    print(f"Friedman: chi2 = {fried_stat:.5f}, p = {fried_p:.5f}")

    anova_summary_rows.append({
        "metric": metric,
        "n_subjects": n_subjects,
        "methods": ",".join(method_order),
        "anova_F": F_val,
        "anova_p": p_val,
        "friedman_chi2": fried_stat,
        "friedman_p": fried_p
    })

    # ----- Pairwise comparisons -----
    pairs = list(itertools.combinations(method_order, 2))
    results = []
    for (m1, m2) in pairs:
        x, y = pivot[m1].values, pivot[m2].values
        t_stat, t_p = stats.ttest_rel(x, y, nan_policy='raise')
        try:
            w_stat, w_p = stats.wilcoxon(x, y)
        except ValueError:
            w_stat, w_p = np.nan, np.nan
        d = paired_cohens_d(x, y)
        ci_lower, ci_upper = bootstrap_mean_diff_ci(x, y, n_boot=N_BOOT, alpha=ALPHA)

        results.append({
            "metric": metric,
            "method_1": m1,
            "method_2": m2,
            "t_stat": t_stat,
            "t_p": t_p,
            "w_stat": w_stat,
            "w_p": w_p,
            "cohen_d_paired": d,
            "mean_diff": (x - y).mean(),
            "ci_lower": ci_lower,
            "ci_upper": ci_upper
        })

    # Holm correction
    if results:
        t_ps = [r["t_p"] for r in results]
        w_ps = [r["w_p"] if not np.isnan(r["w_p"]) else 1.0 for r in results]
        reject_t, t_corr, _, _ = multipletests(t_ps, alpha=ALPHA, method='holm')
        reject_w, w_corr, _, _ = multipletests(w_ps, alpha=ALPHA, method='holm')
        for i, r in enumerate(results):
            r["t_p_corrected_holm"] = t_corr[i]
            r["t_reject_holm"] = bool(reject_t[i])
            r["w_p_corrected_holm"] = w_corr[i]
            r["w_reject_holm"] = bool(reject_w[i])

    posthoc_rows.extend(results)

# ---------------- Save results ----------------
df_anova = pd.DataFrame(anova_summary_rows)
df_posthoc = pd.DataFrame(posthoc_rows)

df_anova.to_csv("stat_tests_summary.csv", index=False)
df_posthoc.to_csv("posthoc_results.csv", index=False)

print("\nSaved:")
print("  - stat_tests_summary.csv")
print("  - posthoc_results.csv")
print("\nPreview of posthoc results:")
print(df_posthoc.head(10).to_string(index=False))
