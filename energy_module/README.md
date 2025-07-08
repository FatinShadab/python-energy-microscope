# Energy Modules

This directory contains scripts, wrappers, and configuration files used to measure **CPU energy consumption** during the execution of Python benchmarks in our study:
**"Python Under the Microscope: A Comparative Energy Analysis of Execution Methods."**

All energy readings are captured via **Intel RAPL** counters using the `pyRAPL` library, providing **precise, reproducible, and software-level energy profiling** on Intel-based systems.


## Directory Structure

```
energy_modules/
├── __pyRAPL__/
│   ├── measure_pyrapl.py       # Benchmark wrapper with pyRAPL decorator
measurement
└── README.md                   # This file
```


## Module Description

| Module              | Description                                                                         |
| ------------------- | ----------------------------------------------------------------------------------- |
| `measure_pyrapl.py` | Core script used to **wrap and execute a benchmark** under energy measurement.      |
| `pyRAPL`            | Python library for accessing **Intel RAPL (Running Average Power Limit)** counters. |
| `setup_pyrapl.md`   | Contains step-by-step setup for configuring permissions and dependencies.           |


## Features

* Uses Intel RAPL to read energy usage in **microjoules (μJ)** for the CPU package.
* Integrates with your benchmark using **Python decorators**, ensuring low overhead.
* Logs energy measurements in **CSV and JSON** for easy downstream analysis.
* Supports batch execution and repeat measurement with consistent sampling conditions.
* Focuses on **runtime-only** power usage (excludes build/compilation energy).

> ⚠️ Only works on Intel-based Linux machines with RAPL access.


## Setup Instructions

Follow the setup guide in [`setup_pyrapl.md`](__pyRAPL__/setup_pyrapl.md) to:

1. Install `pyRAPL`:

   ```bash
   pip install pyRAPL
   ```

2. Ensure access to `/sys/class/powercap/` (requires root or permissions fix):

   ```bash
   sudo chmod -R a+r /sys/class/powercap/intel-rapl:*/energy_uj
   ```

3. (Optional) Set CPU affinity and disable turbo boost for consistent readings.

## Example Usage

To measure the energy usage of a benchmark (e.g., `binary_tree.py`):

```bash
cd energy_modules/__pyRAPL__/

nice -n -20 ionice -c2 -n0 python measure_pyrapl.py ../../benchmarks/Binary-Trees/CPython/binary_tree.py
```

This command:

* Gives high CPU and I/O priority to reduce external noise.
* Executes the benchmark wrapped in a pyRAPL measurement context.
* Saves energy logs to a structured CSV file for post-analysis.

## Output Format

* Output is saved as both `.csv` and `.json`.
* Fields include:

  * **timestamp**
  * **benchmark name**
  * **energy (μJ)**
  * **duration (s)**
  * **package/core/domain (if available)**

## Repetition and Batch Execution

In experiments, each benchmark was run **50 times** to account for natural fluctuations and background processes. You can modify the wrapper to include repetitions or batch folder traversal.

## Notes on Accuracy

* RAPL provides **hardware-level counters** for energy estimation.
* We measure only **CPU Package Power** as DRAM counters are often unavailable on laptops.
* Results were averaged across 50 runs and normalized per algorithm for fair cross-method comparison.