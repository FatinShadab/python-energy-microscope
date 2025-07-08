# Dataset: Python Energy Microscope

This directory contains **benchmark data** collected during the experiments of the paper:
**"Python Under the Microscope: A Comparative Energy Analysis of Execution Methods"**.

It includes **raw measurement logs**, **aggregated performance metrics**, and **normalized values** across five Python execution methods, covering **15 benchmark algorithms**.


## Dataset Access

The complete dataset is also publicly available on Kaggle:

👉 **[Kaggle Dataset Link](https://www.kaggle.com/datasets/fatinshadab/python-energy-microscope-dataset)**

> The Kaggle version is ideal for data analysis, reproducibility testing, and direct import into notebooks or visual tools.


## Directory Structure

```
data/
└── collection_1/
    ├── analysis/       # Final normalized values and GreenScore summaries
    ├── combine/        # Aggregated energy, time, and carbon CSVs (15 algorithms × 5 methods)
    ├── cpython/        # Raw CSV logs for CPython runs (energy + time)
    ├── ctypes/         # Raw CSV logs for ctypes runs
    ├── cython/         # Raw CSV logs for Cython runs
    ├── pycompile/      # Raw CSV logs for py_compile runs
    ├── pypy/           # Raw CSV logs for PyPy runs
    └── input.py        # Utility script for generating controlled input data
```

## Description of Contents

* **Raw CSVs**: Contain timestamped logs of 50 repeated runs per algorithm–method pair.
* **Metrics**: Energy (μJ), Execution Time (s), and Estimated Carbon Emissions (gCO₂eq).
* **Normalized Data**: Used to calculate GreenScore via min–max normalization per algorithm.
* **Analysis Folder**: Final processed results, including method-wise averages and rankings.

## Usage Notes

* All files are formatted for **pandas**-friendly import.
* Folder names match execution method names (`cpython`, `cython`, etc.).
* Reproducibility ensured with fixed inputs, consistent machine, and versioned code.


## Citation

If you use this dataset in your work, please cite:

```bibtex
@dataset{shadab2025microscope,
  author = {Shadab, Md Fatin},
  title  = {Python Energy Microscope Dataset},
  year   = {2025},
  url    = {https://www.kaggle.com/datasets/fatinshadab/python-energy-microscope-dataset}
}
```