# Scripts: Data Processing & GreenScore Computation

This directory contains utility scripts used for data aggregation, energy/time/carbon processing, and final GreenScore computation for the study:

**"Python Under the Microscope: A Comparative Energy Analysis of Execution Methods."**

These scripts enable seamless batch processing and reproducibility of benchmark results.


## Directory Overview

```
scripts/
├── avg_combine.py         # Merge mean energy, time, and carbon files into one
├── carbon.py              # Convert energy (μJ) to carbon emissions (gCO₂e)
├── combine_energy.py      # Combine energy results from all methods into one CSV
├── combine_time.py        # Combine time results from all methods into one CSV
├── energy_avg.py          # Compute per-file average energy usage
├── time_avg.py            # Compute per-file average execution time
├── greenscore.py          # Normalize metrics, compute mean scores, and rank methods by GreenScore
├── std.py                 # Compute standard deviation of energy, time, carbon across methods
└── README.md              # This file
```

## Script Descriptions

| Script              | Description                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------------- |
| `avg_combine.py`    | Combines final means from energy, time, and carbon CSVs into one unified `summary_df`.          |
| `carbon.py`         | Converts energy consumption (in μJ) to estimated carbon emissions (gCO₂e) using global average. |
| `combine_energy.py` | Merges `energy_avg.csv` files from each execution method into one energy comparison table.      |
| `combine_time.py`   | Merges `time_avg.csv` files from each execution method into one time comparison table.          |
| `energy_avg.py`     | Averages `package (uJ)` values across repeated runs in each method/algorithm folder.            |
| `time_avg.py`       | Averages execution time from multiple benchmark runs.                                           |
| `greenscore.py`     | Full pipeline for min–max normalization, per-method averaging, and GreenScore computation.      |
| `std.py`            | Calculates per-method standard deviation for energy, time, and carbon emissions.                |


## GreenScore Workflow

1. Run:

   * `combine_energy.py`
   * `combine_time.py`
   * `carbon.py`

2. Use `avg_combine.py` to merge the three mean files.

3. Run `greenscore.py` to:

   * Normalize each metric (row-wise per algorithm).
   * Average scores across all algorithms per method.
   * Compute GreenScore using the formula:

     $$
     \text{GreenScore} = 0.4 \cdot \text{Energy}_{\text{norm}} + 0.4 \cdot \text{Carbon}_{\text{norm}} + 0.2 \cdot \text{Time}_{\text{norm}}
     $$

4. Review output files:

   * `green_score_components_means.csv`
   * `green_score_ranking.csv`

## Example Usage

To generate normalized sustainability rankings:

```bash
python greenscore.py
```

To combine time CSVs from each method:

```bash
python combine_time.py combined_time.csv
```

To calculate carbon footprint from energy:

```bash
python carbon.py
```

---

## Output Format

All scripts produce CSV files with standard field names:

* `algorithm`, `method`, `energy_mean_μJ`, `carbon_mean_gCO2eq`, `execution_time (s)`
* `green_score`, `energy_std`, `carbon_std`, `time_std`

These are designed for direct use in:

* 📊 Visualization scripts
* 📄 LaTeX tables in the final paper
* 📁 Kaggle dataset uploads


## Notes

* Ensure consistent folder structure when running `combine_*.py` scripts.
* Scripts use **relative paths**. Adjust paths as needed for your environment.
* Carbon intensity is set to `0.000475 gCO₂e/J` based on global averages.