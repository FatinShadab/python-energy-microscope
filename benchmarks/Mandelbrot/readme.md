# Mandelbrot Algorithm
The Mandelbrot algorithm is used to determine whether a given point in the complex plane belongs to the Mandelbrot set. The set is defined by iterating the function:

\[
Z_{n+1} = Z_n^2 + C
\]

where \(Z_0 = 0\) and \(C\) is a complex number. If the absolute value of \(Z_n\) remains bounded after a fixed number of iterations, \(C\) is considered part of the Mandelbrot set.

## Algorithm
1. Select a rectangular region of the complex plane.
2. For each pixel \( (x, y) \), convert it into a complex number \( C \).
3. Initialize \( Z = 0 \).
4. Iterate using the equation \( Z_{n+1} = Z_n^2 + C \).
5. If \( |Z| > 2 \) before reaching the iteration limit, the point is outside the set.
6. Assign a color based on the number of iterations before escape.
7. If the iteration limit is reached, the point belongs to the Mandelbrot set and is usually colored black.
8. Repeat for all pixels to render the fractal.

## Time Complexity
- **Worst Case:** \( O(N) \) per point, where \( N \) is the maximum number of iterations.
- **Best Case:** \( O(1) \), when the escape condition is met quickly.
- **Overall:** \( O(W \times H \times N) \) for an image of width \( W \) and height \( H \).

## Space Complexity
- **Iterative Approach:** \( O(1) \) (only a few variables needed for computation).
- **Storing the Image:** \( O(W \times H) \).

## Implementation Approach
1. **Sequential (Naïve):** Compute each pixel independently in a loop.
2. **Parallelization:** Use multi-threading, SIMD, or GPU-based approaches to improve performance.
3. **Optimized Escape:** Use period detection to reduce unnecessary iterations.
4. **Color Mapping:** Utilize smooth coloring instead of discrete escape iteration count.

## References
- **CLBG (Computer Language Benchmarks Game) Mandelbrot Benchmark**  
  - Official Source: [https://benchmarksgame-team.pages.debian.net/benchmarksgame/](https://benchmarksgame-team.pages.debian.net/benchmarksgame/)
- **Fractals Everywhere by Michael Barnsley**
- **Wikipedia: Mandelbrot Set**  
  - [https://en.wikipedia.org/wiki/Mandelbrot_set](https://en.wikipedia.org/wiki/Mandelbrot_set)
