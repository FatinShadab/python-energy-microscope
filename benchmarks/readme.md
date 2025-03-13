# Benchmarks Research

This directory contains benchmarks for various algorithms, implemented in multiple Python execution methods. Each algorithm is placed in a separate folder with the following structure:

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
├── Fasta/
│   ├── README.md (algorithm explanation)
│   ├── CPython/
│   ├── PyPy/
│   ├── Ctypes/
│   └── Cython/
│
├── K-Nucleotide/
│   ├── README.md (algorithm explanation)
│   ├── CPython/
│   ├── PyPy/
│   ├── Ctypes/
│   └── Cython/
│
├── Mandelbrot/
│   ├── README.md (algorithm explanation)
│   ├── CPython/
│   ├── PyPy/
│   ├── Ctypes/
│   └── Cython/
│
├── N-Body/
│   ├── README.md (algorithm explanation)
│   ├── CPython/
│   ├── PyPy/
│   ├── Ctypes/
│   └── Cython/
│
├── Pi-Digits/
│   ├── README.md (algorithm explanation)
│   ├── CPython/
│   ├── PyPy/
│   ├── Ctypes/
│   └── Cython/
│
├── Regex-Redux/
│   ├── README.md (algorithm explanation)
│   ├── CPython/
│   ├── PyPy/
│   ├── Ctypes/
│   └── Cython/
│
├── Reverse-Complement/
│   ├── README.md (algorithm explanation)
│   ├── CPython/
│   ├── PyPy/
│   ├── Ctypes/
│   └── Cython/
│
├── Spectral-Norm/
│   ├── README.md (algorithm explanation)
│   ├── CPython/
│   ├── PyPy/
│   ├── Ctypes/
│   └── Cython/
│
├── Towers-of-Hanoi/
│   ├── README.md (algorithm explanation)
│   ├── CPython/
│   ├── PyPy/
│   ├── Ctypes/
│   └── Cython/
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

### `README.md` (algorithm explanation)
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

## Algorithm List
> Mixture of various algorithms with algorithms from [CLBG (Computer Language Benchmarks Game)](https://en.wikipedia.org/wiki/The_Computer_Language_Benchmarks_Game)

1. **Binary Trees**
2. **Fannkuch-Redux**
3. **Fasta**
4. **K-Nucleotide**
5. **Mandelbrot**
6. **N-Body**
7. **Pi-Digits**
8. **Regex-Redux**
9. **Reverse-Complement**
10. **Spectral-Norm**
11. **Towers of Hanoi**
12. **N-Queens**