# Energy Modules

This directory contains scripts and utilities for measuring the energy consumption of Python execution methods while running benchmark algorithms. These modules assist in analyzing the efficiency of different Python implementations in terms of power usage.

## Directory Structure

```
energy_modules/
├── pyRAPL/
│   ├── measure_pyrapl.py
│   ├── setup_pyrapl.md
│   └── requirements.txt
├── Intel_RAPL/
│   ├── measure_rapl.py
│   ├── setup_rapl.md
│   └── requirements.txt
├── PowerGadget/
│   ├── measure_powergadget.py
│   ├── setup_powergadget.md
│   └── requirements.txt
└── README.md
```

## Modules

### 1. **pyRAPL**
- Uses the `pyRAPL` library to measure CPU power consumption.
- Requires `pyRAPL` to be installed.
- Supports multiple sampling intervals and logging options.

### 2. **Intel RAPL (Running Average Power Limit)**
- Uses direct access to Intel RAPL power measurement.
- Provides energy readings in microjoules.
- Compatible with Linux systems.

### 3. **Intel Power Gadget**
- Uses Intel Power Gadget to measure energy consumption.
- Works on Windows and macOS.
- Requires Intel Power Gadget software installation.

## Setup Instructions
Each module has its own setup guide (`setup_*.md`) explaining dependencies and installation procedures.

## Usage
Each module contains a `measure_*.py` script that runs a benchmark and records power consumption. Example usage:

```sh
python measure_pyrapl.py <benchmark_script.py>
python measure_rapl.py <benchmark_script.py>
python measure_powergadget.py <benchmark_script.py>
```

## Output
Energy consumption results are typically logged in CSV format for further analysis.