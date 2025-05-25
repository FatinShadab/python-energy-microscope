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
1. **Performance & Efficiency Analysis**
    - Quantify and compare the energy consumption of different Python execution methods.

    - Analyze the trade-offs between execution speed, energy efficiency, and carbon emissions.

    - Measure CPU and memory usage to understand their impact on power consumption.

2. **Practicality & Real-World Application**
    - Evaluate the scalability and practicality of each execution method for real-world applications.

    - Assess the ease of implementation of different execution methods.

3. **Sustainability & Green Computing**
    - Contribute to sustainable computing by identifying the most eco-friendly and efficient Python execution models.

## **Research Questions**  
- **Which Python execution method demonstrates the highest energy efficiency when executing pure Python code with minimal third-party libraries?**
- **What is the relationship between execution speed and energy consumption across different Python execution methods?**
- **Which Python execution method has the lowest carbon footprint according to software energy profiling?**

## **Benchmarking & Methodology**  
This study employs **a modified set of Computer Language Benchmarks Game (CLBG) algorithms**, blending standard performance benchmarks with **additional real-world computational tasks**. The benchmarking ensures **fair and consistent execution across all runtime environments** while maintaining **minimal dependencies** for pure execution measurement.

### **Step 1: Input Acquisition**

The study begins by collecting three core performance metrics for each algorithm–method pair: energy consumption (in microjoules), execution time (in seconds), and estimated carbon footprint (in grams of CO₂ equivalent). These measurements are stored in structured tabular format, where each row represents a unique algorithm and each column corresponds to one of the evaluated Python execution methods.


### **Step 2: Row-Wise Normalization of Metrics**

To enable fair cross-method comparison within each algorithm, all metrics are normalized on a **per-algorithm (row-wise)** basis using **min-max normalization**. For a given metric (energy, carbon, or time), the normalized score for a method $x$ within an algorithm row is computed as:

$$
\text{Normalized Value} = \frac{x - \min(\text{row})}{\max(\text{row}) - \min(\text{row})}
$$

This transformation ensures consistency in interpretation:

* A normalized value of **0.0** denotes the **best performing method** for that algorithm (i.e., lowest energy, carbon, or time).
* A normalized value of **1.0** indicates the **worst performing method** for that algorithm.

This step preserves the relative performance ranking within each algorithm while eliminating the effects of differing value scales across metrics.


### **Step 3: Per-Method Metric Averaging**

After normalization, each method's overall performance is aggregated by computing the **mean normalized score** across all algorithms. Specifically, the following averages are calculated for every execution method:

* **Mean normalized energy**
* **Mean normalized carbon emission**
* **Mean normalized execution time**

These averages provide a high-level summary of each method’s behavior across the complete algorithm suite.


### **Step 4: Composite GreenScore Calculation**

To holistically evaluate the sustainability of each method, the normalized scores for energy, carbon, and time are combined into a single scalar value known as the **GreenScore**. This composite score is computed using a **weighted linear combination**:

$$
\text{GreenScore} = \alpha \cdot \text{Energy} + \beta \cdot \text{Carbon} + \gamma \cdot \text{Time}
$$

Where:

* $\alpha = 0.4$: weight for energy efficiency
* $\beta = 0.4$: weight for carbon impact
* $\gamma = 0.2$: weight for execution time
* $\alpha + \beta + \gamma = 1.0$

These weights can be tuned to reflect specific sustainability goals (e.g., prioritizing carbon reduction over speed), but the chosen default emphasizes energy and carbon equally, with a smaller consideration for runtime performance.


### **Step 5: Method Ranking**

Finally, all execution methods are ranked in **ascending order of their GreenScore**, where:

* A **lower GreenScore** indicates a **more sustainable and efficient execution method**.
* The method ranked **first** is interpreted as the **greenest choice overall**, balancing energy consumption, environmental impact, and performance.

This ranking provides developers and researchers with actionable insight into which Python execution strategies are most aligned with sustainability goals.

### **Test Cases**  
- **CLBG Algorithms (Modified)**: Binary Trees, Mandelbrot, N-Body, Regex-Redux, Spectral-Norm  
- **Algorithmic Workloads**: N-Queens, Towers of Hanoi etc
- **Memory-Intensive Operations**: List vs. NumPy vs. Pandas operations  
- **I/O & Threading Performance**: File Read/Write, Multi-threading  

### **Tools Used**  
- **Energy Measurement**: Intel RAPL/ pyRAPL  
- **Time Profiling**: `time`
- **Data Analysis**: Matplotlib, Pandas

## **Important Repository Structure**  
```
/benchmarks      # Modified CLBG and other algorithms and additional benchmarks  
/energy_modules  # Scripts to measure power consumption  
/time_modules    # Scripts to measure execution time
/visualization   # Scripts to visualize the mesurement  
```

## **Getting Started**  
To run the benchmarks, clone the repository and follow the instructions below,

```bash
git clone https://github.com/your-repo/python-energy-microscope.git
cd python-energy-microscope
```

## **Key Highlights of This Research**  
- Uses modified CLBG algorithms for robust benchmarking.  
- No third-party Python libraries – Focused on **pure execution measurement**.  
- Compares multiple execution models, filling a research gap.  
- **Software-based** energy measurement.
- Ranking multiple execution models based on **carbon footprint**.
- Sustainable computing approach, contributing to green software engineering.  

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
