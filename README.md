# **Python Under the Microscope: A Comparative Energy Analysis of Execution Methods**  

**Welcome to Python Energy Microscope.** This repository contains research code, benchmarks, and energy measurement scripts for the study **"Python Under the Microscope: A Comparative Energy Analysis of Execution Methods."**  

## **Overview**  
With growing concerns about **sustainable computing**, this study examines the **energy efficiency of different Python execution methods** to determine the most **energy-efficient (greenest) approach**.  

- **CPython** (Standard Interpreter)  
- **PyPy** (JIT Compilation)  
- **CPython + Cython** (Ahead-of-Time Compilation)  
- **CPython + ctypes** (Foreign Function Interface)  
- **py_compile** (Bytecode Compilation)  

This study provides an **empirical energy consumption analysis** of these execution methods using **software-based energy measurement tools**.

## **Research Objectives**  
- **Quantify** energy consumption across Python execution methods.  
- **Analyze trade-offs** between execution speed and energy efficiency.  
- **Measure CPU & memory usage** to understand power consumption.  
- **Contribute to sustainable computing** by identifying optimal execution models.  

## **Benchmarking & Methodology**  
This study employs **a modified set of Computer Language Benchmarks Game (CLBG) algorithms**, blending standard performance benchmarks with **additional real-world computational tasks**. The benchmarking ensures **fair and consistent execution across all runtime environments** while maintaining **minimal dependencies** for pure execution measurement.

### **Test Cases**  
- **CLBG Algorithms (Modified)**: Binary Trees, Mandelbrot, N-Body, Regex-Redux, Spectral-Norm  
- **Algorithmic Workloads**: N-Queens, Towers of Hanoi etc
- **Memory-Intensive Operations**: List vs. NumPy vs. Pandas operations  
- **I/O & Threading Performance**: File Read/Write, Multi-threading  

### **Tools Used**  
- **Energy Measurement**: Intel RAPL, Intel Power Gadget, pyRAPL  
- **Performance Profiling**: `timeit`, `memory_profiler`, `cProfile`  
- **Data Analysis**: Matplotlib, Pandas  

## **Repository Structure**  
```
/benchmarks      # Modified CLBG and other algorithms and additional benchmarks  
/energy_  # Scripts to measure power consumption  

/docs           # Docsify documentation files  
README.md       # Landing page for Docsify  
```

## **Getting Started**  
To run the benchmarks, clone the repository and follow the instructions below,

```bash
git clone https://github.com/your-repo/python-energy-microscope.git
cd python-energy-microscope
```

---

## **Key Highlights of This Research**  
- Uses modified CLBG algorithms for robust benchmarking.  
- No third-party Python libraries – Focused on **pure execution measurement**.  
- Compares multiple execution models, filling a research gap.  
- Hardware-based energy measurement for accurate results.  
- Sustainable computing approach, contributing to green software engineering.  