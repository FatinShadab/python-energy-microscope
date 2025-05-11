# mandelbrot_cy.pyx
cdef inline int mandelbrot(double real, double imag, int max_iter):
    cdef double z_real = 0.0
    cdef double z_imag = 0.0
    cdef double z_real_sq, z_imag_sq
    cdef int i

    for i in range(max_iter):
        z_real_sq = z_real * z_real
        z_imag_sq = z_imag * z_imag
        if z_real_sq + z_imag_sq > 4.0:
            return i
        z_imag = 2.0 * z_real * z_imag + imag
        z_real = z_real_sq - z_imag_sq + real
    return max_iter

def generate_mandelbrot(int width, int height, int max_iter,
                        double x_min, double x_max, double y_min, double y_max):
    cdef double aspect_ratio = width / height
    y_min /= aspect_ratio
    y_max /= aspect_ratio

    cdef int x, y
    cdef double real, imag
    cdef list mandelbrot_set = []
    cdef list row

    for y in range(height):
        row = []
        for x in range(width):
            real = x_min + (x / width) * (x_max - x_min)
            imag = y_min + (y / height) * (y_max - y_min)
            row.append(mandelbrot(real, imag, max_iter))
        mandelbrot_set.append(row)
    
    return mandelbrot_set
