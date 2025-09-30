import pandas as pd
import glob
from scipy.stats import f_oneway, kendalltau
import csv

# --------------------------------------------------------------------------
# Step 1: Load all CSV files containing GreenScore data for different weight combinations
# --------------------------------------------------------------------------
# Adjust the path pattern to match your file location
files = glob.glob("..\\data\\collection_1\\analysis\\green_score_weight_anova\\green_score_ranking_*.csv")

# Dictionaries to store GreenScore values and rankings for each weight combination
scores = {}    # key: weight combination string, value: array of GreenScore values
rankings = {}  # key: weight combination string, value: ranking array (1 = highest)

# Loop over all files and read data
for file in files:
    df = pd.read_csv(file)  # Read CSV file into pandas DataFrame
    weight_key = file.split("green_score_ranking_")[1].replace(".csv", "")  # Extract weight combination name
    scores[weight_key] = df['green_score'].values  # Store GreenScore values
    # Store ranking (1 = highest GreenScore)
    rankings[weight_key] = df['green_score'].rank(ascending=False).values

# --------------------------------------------------------------------------
# Step 2: Perform global one-way ANOVA across all weight combinations
# --------------------------------------------------------------------------
# f_oneway compares means across multiple groups (weight sets)
anova_result = f_oneway(*scores.values())

print("One-way ANOVA across weight sets:")
print(f"F-statistic: {anova_result.statistic:.5f}")
print(f"p-value: {anova_result.pvalue:.5f}\n")

# --------------------------------------------------------------------------
# Step 3: Perform pairwise comparison vs default weighting (0.4, 0.4, 0.2)
# --------------------------------------------------------------------------
# Define the default weight key
default_key = "a0_4_b0_4_g0_2"
default_scores = scores[default_key]
default_ranking = rankings[default_key]

# Store output rows to save as CSV later
output_rows = []

print("Pairwise comparison vs default weighting (0.4, 0.4, 0.2):\n")

for key, values in scores.items():
    if key != default_key:
        # Compute ANOVA between default weights and this weight combination
        stat, p = f_oneway(default_scores, values)
        # Compute Kendall's tau correlation to compare ranking stability
        tau, tau_p = kendalltau(default_ranking, rankings[key])
        
        # Parse alpha, beta, gamma values from the weight key string
        # key format: a0_4_b0_4_g0_2
        alpha = key.split('_')[0][1:] + '.' + key.split('_')[1]
        beta = key.split('_')[2][1:] + '.' + key.split('_')[3]
        gama = key.split('_')[4][1:] + '.' + key.split('_')[5]
        
        # Append results to output list
        output_rows.append([alpha, beta, gama, f"{stat:.5f}", f"{p:.5f}", f"{tau:.3f}", f"{tau_p:.5f}"])
        
        # Print results
        print(f"Default vs {key}: F = {stat:.5f}, p = {p:.5f}, Kendall τ = {tau:.3f}, p = {tau_p:.5f}")

# --------------------------------------------------------------------------
# Step 4: Save pairwise comparison results to CSV
# --------------------------------------------------------------------------
with open("anova_pairwise_output.csv", "w", newline='') as f:
    writer = csv.writer(f)
    # Write header
    writer.writerow(["alpha", "beta", "gama", "F", "p", "Kendall", "tau_p"])
    # Write all data rows
    writer.writerows(output_rows)
