# Python Under the Microscope: A Comparative Energy Analysis of Execution Methods

Welcome to Python Energy Microscope. This repository contains source code, benchmarks, and energy profiling tools for our research study: **"Python Under the Microscope: A Comparative Energy Analysis of Execution Methods."**

## Overview

As Python remains one of the most widely used programming languages, it's crucial to understand the sustainability implications of different ways to execute Python code. This study conducts a fine-grained comparison of five execution methods in terms of energy consumption, runtime performance, and carbon footprint:

* **CPython** (standard interpreter)
* **PyPy** (Just-In-Time compiler)
* **Cython** (Ahead-of-Time compiler)
* **ctypes** (Foreign Function Interface to native C code)
* **py\_compile** (Bytecode compilation)

Using a reproducible benchmarking setup and 15 diverse CPU-bound algorithms, we rank these methods by their overall sustainability using a novel metric called **GreenScore**.

## Research Objectives

1. **Energy & Environmental Profiling**

   * Quantitatively compare execution time, energy consumption, and CO₂ emissions across Python execution methods.
2. **Sustainable Runtime Selection**

   * Identify the most eco-friendly execution strategy for Python workloads.
3. **Benchmark-Driven Insights**

   * Establish a reproducible, algorithmically diverse benchmark suite reflective of real-world Python usage.

## Research Questions

* Which execution method offers the best balance between speed, energy use, and carbon emissions?
* How do interpreted, compiled, and hybrid execution strategies differ in sustainability?
* Can a unified metric fairly rank Python methods by environmental impact?

## Benchmarking Methodology

This study uses a set of 15 CPU-bound algorithms, including 10 adapted from the **Computer Language Benchmarks Game (CLBG)** and 5 supplementary tasks. Each algorithm is implemented identically across all execution strategies.

### Execution Methods

* CPython 3.13.2
* PyPy 7.3.19 (Python 3.11.11 compatible)
* Cython 3.0.12 with static typing support
* ctypes via shared native C libraries
* py\_compile with optimization level 2

### Measurement Tools

* **Energy:** pyRAPL (Intel RAPL counters)
* **Runtime:** Python's `time.time()`
* **Carbon Footprint:** Based on global average carbon intensity (0.000475 gCO₂e/J)

## GreenScore: Composite Metric

To compare methods holistically, we introduce **GreenScore**, a weighted composite score that integrates energy, carbon, and time:

```math
\text{GreenScore} = \alpha \cdot \text{Energy}_{\text{norm}} + \beta \cdot \text{Carbon}_{\text{norm}} + \gamma \cdot \text{Time}_{\text{norm}}
```

Where: $\alpha = 0.4$, $\beta = 0.4$, $\gamma = 0.2$.

* All metrics are normalized per-algorithm (min-max normalization).
* Each execution method's average normalized metrics are aggregated across 15 algorithms.
* Lower GreenScore = better overall sustainability.

### Example:

For the `ctypes` method:

```math
\text{Energy}_{\text{norm}} = 0.162,\ \text{Carbon}_{\text{norm}} = 0.193,\ \text{Time}_{\text{norm}} = 0.123
```

```math
\text{GreenScore}_{\texttt{ctypes}} = 0.4 \cdot 0.162 + 0.4 \cdot 0.193 + 0.2 \cdot 0.123 = \textbf{0.1666}
```

This was the **lowest score**, confirming `ctypes` as the greenest Python method.

## Results Summary

* **ctypes** achieved the best overall sustainability.
* **PyPy** excelled in long-running loops due to JIT.
* **Cython** provided consistent performance gains but higher compilation overhead.
* **CPython** and **py\_compile** served as baselines but showed lower efficiency.

## Reproducibility

* Benchmarks repeated 50 times per method-algorithm pair.
* Dataset of 75 combinations (15 algorithms x 5 methods) provided in `/data`.
* All measurements performed on Intel-based laptop running Ubuntu.

## Repository Structure

```
/benchmarks         # All 15 algorithm implementations
/energy_modules     # pyRAPL wrappers and logging scripts
/time_modules       # Execution time measurement
/visualization      # Bar charts, line graphs, scatter plots
/data               # Normalized and raw benchmark outputs
```

## Visual Diagrams

### 1. Architecture Diagram

![arch](https://github.com/FatinShadab/python-energy-microscope/blob/main/assets/arch.jpg)

### 2. Benchmarking Flowchart

![flowchart](https://github.com/FatinShadab/python-energy-microscope/blob/main/assets/flowchart.jpg)

### 3. Sequence Diagram

![sequence](https://github.com/FatinShadab/python-energy-microscope/blob/main/assets/sequence_diagram.jpg)

## Getting Started

```bash
git clone https://github.com/FatinShadab/python-energy-microscope.git
cd python-energy-microscope
python3 run_benchmarks.py
```

## Citation

If you use this work, please cite:

```
@article{shadab2025microscope,
  title   = {Python Under the Microscope: A Comparative Energy Analysis of Execution Methods},
  author  = {Shadab, Md Fatin and Others},
  journal = {__},
  year    = {2025}
}
```

---

This research was conducted as part of **EEE 4261 (Green Computing)** offered at United International University in Spring 2025. All code, data, and visualization tools are released for reproducibility and open sustainability research.
