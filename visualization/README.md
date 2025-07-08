# Visualization Modules

This directory contains visualization scripts for generating plots and graphs based on performance, energy, and sustainability metrics from our study:
**"Python Under the Microscope: A Comparative Energy Analysis of Execution Methods."**

These tools help convert raw measurement data into clear, publication-ready figures, enabling comparative analysis across Python execution methods using energy, time, and carbon emission metrics.

## Directory Structure

```
visualization/
├── visualize_metrics.py         # Core script for generating all charts
└── README.md                    # This file
```

## Module Description

| Script                 | Description                                                                 |
| ---------------------- | --------------------------------------------------------------------------- |
| `visualize_metrics.py` | Command-line tool for generating line charts, bar charts, and scatter plots |
| `matplotlib`, `pandas` | Used for plotting and CSV data handling                                     |
| `argparse`             | CLI interface to flexibly choose the desired chart                          |

## Features

* Plots **grouped bar charts** comparing energy, time, and carbon across execution methods
* Plots **line charts** of energy, time, and carbon trends per algorithm
* Plots **scatter plot** showing relationship between energy and execution time
* Normalizes data where necessary for fair visual comparison
* CLI options to control chart type and input files
* Produces **PNG outputs** ready for publication or report integration

## Setup Instructions

Install required Python libraries if not already available:

```bash
pip install matplotlib pandas numpy
```

## Chart Types & CLI Flags

| Flag             | Description                                                                               |
| ---------------- | ----------------------------------------------------------------------------------------- |
| `--evcvt`        | Generates grouped bar chart (Energy vs Carbon vs Time by method)                          |
| `--lcpack`       | Line charts of energy, time, and carbon for each algorithm                                |
| `--scatter`      | Scatter plot showing execution time vs energy consumption (`--scatter <energy> <time>`)   |
| `--line_compare` | Overlayed line chart comparing energy and time for each method (`--line_compare <e> <t>`) |
| `--etc_compare`  | Summary line chart of mean energy/time per method (combined)                              |


## Example Usage

### 1. Grouped Bar Chart

```bash
python visualize_metrics.py energy_vs_carbon_vs_time.csv --evcvt --output_file evcvt_bar.png
```

### 2. Line Charts of Energy/Time/Carbon (by algorithm)

```bash
python visualize_metrics.py --lcpack
```

### 3. Scatter Plot (Energy vs Time per Algorithm)

```bash
python visualize_metrics.py --scatter energy_com.csv time_com.csv --output_file scatter_energy_time.png
```

### 4. Comparative Line Chart: Energy & Time (per method)

```bash
python visualize_metrics.py --line_compare energy_com.csv time_com.csv --output_file comparison_linechart.png
```

## Output Examples

* `evcvt_bar.png`: Grouped bar chart of execution metrics
* `line_energy_per_algorithm.png`: Energy usage per algorithm
* `line_carbon_per_algorithm.png`: Carbon emissions by algorithm
* `scatter_energy_time.png`: Per-algorithm energy vs time scatter plot
* `method_metric_comparison_linechart.png`: Combined trends across execution methods


## Notes on Visualization

* Bar chart normalization: $x_{\text{norm}} = \frac{x}{\max(x)}$
* Line plots include method legends and algorithm-specific breakdowns
* Scatter plots annotate algorithms and color points by method

> These visualizations were used in the Results section of our paper to compare execution models.