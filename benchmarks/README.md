# **Benchmarks Research**

This directory contains the benchmark implementations used in our study:
**“Python Under the Microscope: A Comparative Energy Analysis of Execution Methods.”**
The benchmarks are designed to be minimal, CPU-bound, and reproducible across multiple Python execution methods.


## **Benchmark Suite Overview**

The benchmark set includes **15 diverse, compute-intensive algorithms**, combining:

* ✅ **10 standard programs** adapted from the [Computer Language Benchmarks Game (CLBG)](https://benchmarksgame-team.pages.debian.net/benchmarksgame/index.html)
* ✅ **5 additional algorithms** selected for recursive, matrix, and search-based operations

These tasks were chosen to evaluate energy, carbon, and runtime metrics across Python execution methods in a controlled setup.

### CLBG-Based Algorithms (10)

| No. | Algorithm          | Description                                                       |
| --- | ------------------ | ----------------------------------------------------------------- |
| 1   | Binary Trees       | Builds and recursively traverses trees to test memory & recursion |
| 2   | Fannkuch-Redux     | Permutation-based benchmarking of loops and array access          |
| 3   | Fasta              | Generates pseudo-DNA sequences for bioinformatics-like workloads  |
| 4   | K-Nucleotide       | Frequency counting of substrings in DNA sequences                 |
| 5   | Mandelbrot         | Computes complex numbers in nested loops to render fractals       |
| 6   | N-Body             | Physics-based simulation of gravitational forces                  |
| 7   | Pi-Digits          | Spigot algorithm for calculating digits of Pi                     |
| 8   | Regex-Redux        | Regular expression substitution over large genomic text           |
| 9   | Reverse-Complement | Memory-heavy string processing for DNA strand reversal            |
| 10  | Spectral-Norm      | Matrix-vector multiplication and spectral norm estimation         |


### Supplementary Algorithms (5)

| No. | Algorithm             | Description                                                        |
| --- | --------------------- | ------------------------------------------------------------------ |
| 11  | K-Nearest Neighbors   | Distance-based classification to evaluate memory and data locality |
| 12  | N-Queens              | Recursive backtracking for constraint satisfaction problems        |
| 13  | Strassen              | Divide-and-conquer matrix multiplication                           |
| 14  | Towers of Hanoi       | Classic recursion-heavy puzzle to test deep call stacks            |
| 15  | Sieve of Eratosthenes | Prime number generation using array filtering loops                |


## **Directory Structure**

Each algorithm has its own folder containing identical implementations (logic preserved) across the five Python execution methods:

```bash
benchmarks/
├── Binary-Trees/
│   ├── README.md         # Algorithm explanation, input/output, and complexity
│   ├── CPython/          # Standard interpreter
│   ├── PyPy/             # Compatible with PyPy JIT runtime
│   ├── Ctypes/           # Uses shared C libraries and FFI via ctypes
│   ├── Cython/           # Optimized AOT-compiled Python
│   └── py_compile/       # Precompiled .pyc bytecode form (Python optimize mode)
│
├── Mandelbrot/
│   └── ...
└── ...
```

---

## Inside Each Algorithm Folder

| Component     | Description                                                                |
| ------------- | -------------------------------------------------------------------------- |
| `README.md`   | Short description of the algorithm, input size, and runtime complexity     |
| `CPython/`    | Unmodified Python version for baseline measurements                        |
| `PyPy/`       | Same script, evaluated under the PyPy JIT runtime                          |
| `Ctypes/`     | Python script + `.c` source code + `setup.py` or `Makefile` for C bindings |
| `Cython/`     | `.pyx` source, `setup.py`, and compiled extension module                   |
| `py_compile/` | Same as CPython, but executed from compiled `.pyc` bytecode                |

---

## Execution Consistency Notes

* All implementations are functionally identical across methods.
* Inputs are fixed and preloaded to reduce I/O impact.
* Only CPU-intensive logic is measured—no disk, network, or third-party packages.
* Timing and energy profiling are wrapped using consistent decorators.

---

## Example Structure: `Binary-Trees`

```
benchmarks/
└── Binary-Trees/
    ├── README.md
    ├── CPython/
    │   └── binary_tree.py
    ├── PyPy/
    │   └── binary_tree.py
    ├── Ctypes/
    │   ├── binary_tree_ctypes.py
    │   ├── tree.c
    │   └── setup.py
    ├── Cython/
    │   ├── binary_tree.pyx
    │   └── setup.py
    └── py_compile/
        └── binary_tree.py
```

---

## Reproducibility

* Every folder contains a self-contained benchmark that can be run using the measurement scripts.
* Each run generates logs in `.csv` and `.json` format for energy, time, and carbon estimation.

For setup instructions, refer to the top-level [README.md](../README.md)