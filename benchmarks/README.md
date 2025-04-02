# Benchmarks Research

This directory contains benchmarks for various algorithms, implemented in multiple Python execution methods.

## Algorithm List
> Mixture of various algorithms with algorithms from [CLBG (Computer Language Benchmarks Game)](https://benchmarksgame-team.pages.debian.net/benchmarksgame/index.html)

- **CLBG Algorithms**
    1. Binary Trees
    2. Fannkuch-Redux
    3. Fasta
    4. K-Nucleotide
    5. Mandelbrot
    6. N-Body
    7. Pi-Digits
    8. Regex-Redux
    9. Reverse-Complement
    10. Spectral-Norm
- **Extra Algorithms**
    1. KNN
    2. N-Queens
    3. Strassen
    4. Towers of Hanoi
    5. Sieve-of-Eratosthenes

## Directory Structure

Each algorithm is placed in a separate folder with the following structure:

```
benchmarks/
│
├── Binary-Trees/
│   ├── README.md (algorithm explanation)
│   ├── CPython/
│   ├── PyPy/
│   ├── Ctypes/
│   └── Cython/
│
├── Fannkuch-Redux/
│   ├── README.md (algorithm explanation)
│   ├── CPython/
│   ├── PyPy/
│   ├── Ctypes/
│   └── Cython/
│
...
...
│
└── N-Queens/
    ├── README.md (algorithm explanation)
    ├── CPython/
    ├── PyPy/
    ├── Ctypes/
    └── Cython/
```

## Algorithm Folders

Each algorithm has its own folder with the following structure:

### `README.md` (Algorithm Explanation)
This file explains the **algorithm**, its **use case**, and **overview**. It may also provide information on the **input/output** and **complexity** of the algorithm.

### Implementation Folders (CPython, PyPy, Ctypes, Cython)
Each algorithm has four subfolders for implementation in different execution environments:

- **CPython**: Standard Python implementation.
- **PyPy**: PyPy-specific optimizations (usually no changes needed, but marked for the purpose of this research).
- **Ctypes**: Implementation using C libraries and Python's `ctypes` library for low-level memory management.
- **Cython**: Implementation using Cython for optimized performance by converting Python code to C.

## Example Folder Structure for One Algorithm (Binary-Trees)

```
benchmarks/
└── Binary-Trees/
    ├── README.md
    ├── CPython/
    │   └── binary_tree.py
    ├── PyPy/
    │   └── binary_tree.py
    ├── Ctypes/
    │   └── binary_tree_ctypes.py
    └── Cython/
        └── binary_tree.pyx
```

---

## **Diagrams**

To better understand the execution and benchmarking process, the following diagrams are included:

### **1. Software Architecture Diagram**
- Provides a high-level overview of the execution workflow.
- Illustrates how different execution methods (CPython, PyPy, Cython, Ctypes) interact with the benchmarking system.
- Shows the integration with energy measurement tools (Intel RAPL, Power Gadget, pyRAPL).

![diagram](https://github.com/FatinShadab/python-energy-microscope/blob/main/assets/arch.jpg)

### **2. Flowchart (Benchmarking & Execution Process)**
- Describes the step-by-step process for running benchmarks.
- Includes algorithm selection, execution under different environments, data collection, and visualization.
- Helps in understanding how energy measurements are captured and analyzed.

![diagram](https://github.com/FatinShadab/python-energy-microscope/blob/main/assets/flowchart.jpg)

### **3. Sequence Diagram (Execution & Profiling Steps)**
- Provides a detailed interaction sequence between different components.
- Captures the sequence of operations between benchmarking scripts, execution environments, profiling tools, and data visualization.
- Ensures clarity in how each execution method is tested.

![diagram](https://github.com/FatinShadab/python-energy-microscope/blob/main/assets/sequence_diagram.jpg)
