# Pi Digits
The digits of Pi (π) represent the decimal expansion of the mathematical constant π, which is the ratio of a circle's circumference to its diameter. It is an **irrational number**, meaning it has an **infinite, non-repeating** decimal expansion.

## Algorithm: Gauss-Legendre Method
The **Gauss-Legendre algorithm** is an iterative numerical method for computing Pi that **converges quadratically**, meaning the number of correct digits roughly doubles in each iteration. It is computationally efficient and works well without requiring third-party libraries.

### Steps:
1. Initialize:
   \[
   a_0 = 1, \quad b_0 = \frac{1}{\sqrt{2}}, \quad t_0 = \frac{1}{4}, \quad p_0 = 1
   \]
2. Iterate until the desired precision is reached:
   \[
   a_{n+1} = \frac{a_n + b_n}{2}
   \]
   \[
   b_{n+1} = \sqrt{a_n \cdot b_n}
   \]
   \[
   t_{n+1} = t_n - p_n (a_n - a_{n+1})^2
   \]
   \[
   p_{n+1} = 2p_n
   \]
3. Compute Pi approximation:
   \[
   \pi_n \approx \frac{(a_n + b_n)^2}{4t_n}
   \]

## Time Complexity
The Gauss-Legendre algorithm converges **quadratically**, making it much faster than simple series expansions like Leibniz or Monte Carlo methods.

| Algorithm | Time Complexity |
|-----------|----------------|
| Gauss-Legendre | \(O(n \log n)\) |

## Space Complexity
| Algorithm | Space Complexity |
|-----------|------------------|
| Gauss-Legendre | \(O(\log n)\) |

## Implementation Approach
1. **Use only built-in Python libraries** (no NumPy, SymPy, etc.).
2. **Optimize arithmetic operations** using Python’s built-in floating-point arithmetic.

## References
1. Borwein, J. M., & Borwein, P. B. (1987). *Pi and the AGM: A study in analytic number theory and computational complexity*. Wiley.
2. Bailey, D. H., Borwein, J. M., & Plouffe, S. (1997). "On the rapid computation of various polylogarithmic constants". *Mathematics of Computation*, 66(218), 903-913.
3. Brent, R. P. (1976). *Fast Multiple-Precision Evaluation of Elementary Functions*. Journal of the ACM, 23(2), 242-251.


## Why Gauss-Legendre?
- **No third-party dependencies** needed.
- **Fast convergence**, reducing execution time.
- **Iterative nature**, making it easy to analyze performance across CPython, PyPy, and Cython.
- **Uses basic floating-point operations**, ideal for benchmarking different interpreters' arithmetic performance.