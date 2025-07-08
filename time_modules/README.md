# Time Modules

This directory contains scripts and decorators used to measure **execution time** during benchmark runs in our study:
**"Python Under the Microscope: A Comparative Energy Analysis of Execution Methods."**

All time readings are collected using Python’s native `time.time()` method, offering **lightweight, reproducible, and fine-grained runtime profiling** with minimal overhead.


## Directory Structure

```
time_modules/
├── measure_time_to_csv.py     # Benchmark decorator for time logging
└── README.md                  # This file
```


## Module Description

| Module                   | Description                                                                   |
| ------------------------ | ----------------------------------------------------------------------------- |
| `measure_time_to_csv.py` | Decorator-based utility to **wrap benchmark functions** and log their runtime |
| `time.time()`            | Standard Python function used for **wall-clock time measurement**             |
| `psutil` + `platform`    | Libraries used to log system configuration during measurement                 |


## Features

* Measures runtime in **seconds** using `time.time()` with microsecond resolution.
* Executes the benchmark **n times**, logs each repetition’s duration in a structured CSV.
* Automatically logs **system information** (CPU, RAM, OS, architecture) into a JSON file.
* Output is saved per benchmark, and organized under a dedicated folder (`time_benchmark/`).
* Suitable for measuring short or long-running CPU-bound Python scripts.


## Setup Instructions

This module uses only standard Python libraries except for `psutil`. Install it as follows:

```bash
pip install psutil
```

No root privileges or platform-specific configurations are required.


## Example Usage

```python
from measure_time_to_csv import measure_time_to_csv

@measure_time_to_csv(n=50, csv_filename="binary_tree", folder_name="time_benchmark")
def run_binary_tree():
    # Your benchmark logic here
    pass

run_binary_tree()
```

This will:

* Run the `run_binary_tree()` function 50 times
* Save results to `time_benchmark/binary_tree.csv`
* Save system metadata to `time_benchmark/system_info.json`


## Output Format

### `CSV`: Per-run execution log

| timestamp           | function          | run | execution\_time (s) |
| ------------------- | ----------------- | --- | ------------------- |
| 2025-07-09T08:32:01 | run\_binary\_tree | 1   | 0.01873             |
| ...                 | ...               | ... | ...                 |

### `JSON`: System information

```json
{
  "CPU": "Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz",
  "RAM_GB": 15.85,
  "OS": "Linux 5.15.0-91-generic",
  "Architecture": "x86_64",
  "Test_Result_File": "time_benchmark/binary_tree.csv"
}
```


## Repetition and Statistical Significance

In this study, each benchmark was executed **50 times** to reduce noise and improve result stability. This helps account for background processes, thermal variations, and OS scheduling effects.


## Notes on Accuracy

* `time.time()` captures **wall-clock duration**, which is suitable for coarse-grained benchmarking.
* Results were averaged across runs, then normalized per algorithm for **GreenScore** computation.
* While not cycle-accurate like hardware timers, this approach provides consistent, cross-platform results suitable for comparative analysis.