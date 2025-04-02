# Energy Modules

This directory contains scripts and utilities for measuring the energy consumption of Python execution methods while running benchmark algorithms. These modules assist in analyzing the efficiency of different Python implementations in terms of power usage.

## Directory Structure

```
energy_modules/
├── __pyRAPL__/
│   ├── measure_pyrapl.py
│   ├── setup_pyrapl.md
│   └── requirements.txt
└── README.md
```

## Module
- Uses the `pyRAPL` library to measure CPU power consumption.
- Requires `pyRAPL` to be installed.
- Supports multiple sampling intervals and logging options.
- uses **Intel RAPL (Running Average Power Limit)**

## Setup Instructions
Each module has its own setup guide (`setup_*.md`) explaining dependencies and installation procedures.

## Usage
Each module contains a `measure_*.py` script that runs a benchmark and records power consumption. Example usage:

```sh
python measure_pyrapl.py <benchmark_script.py>
```

## Output
Energy consumption results are typically logged in CSV format for further analysis.