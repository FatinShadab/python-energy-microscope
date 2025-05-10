// mandelbrot.c
#include <stdlib.h>
#include <complex.h>

// Generate the Mandelbrot set and fill a pre-allocated 2D array
void generate_mandelbrot(int width, int height, int max_iter,
                         double x_min, double x_max,
                         double y_min, double y_max,
                         int* output) {
    double aspect_ratio = (double)width / height;
    y_min /= aspect_ratio;
    y_max /= aspect_ratio;

    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            double real = x_min + ((double)x / width) * (x_max - x_min);
            double imag = y_min + ((double)y / height) * (y_max - y_min);
            double complex c = real + imag * I;
            double complex z = 0.0;
            int iter;
            for (iter = 0; iter < max_iter; iter++) {
                z = z * z + c;
                if (cabs(z) > 2.0)
                    break;
            }
            output[y * width + x] = iter;
        }
    }
}
