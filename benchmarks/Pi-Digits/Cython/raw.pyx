# pi_gauss_legendre.pyx
from libc.math cimport sqrt

cpdef double compute_pi_gauss_legendre(int iterations = 10):
    """
    Computes an approximation of Pi using the Gauss-Legendre algorithm.

    Parameters:
    iterations (int): The number of iterations to perform.

    Returns:
    double: The computed value of Pi.
    """
    cdef double a = 1.0
    cdef double b = 1.0 / sqrt(2.0)
    cdef double t = 0.25
    cdef double p = 1.0
    cdef double a_next
    cdef int i

    for i in range(iterations):
        a_next = (a + b) / 2.0
        b = sqrt(a * b)
        t -= p * (a - a_next) * (a - a_next)
        a = a_next
        p *= 2.0

    return ((a + b) * (a + b)) / (4.0 * t)
