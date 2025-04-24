#include <math.h>

double compute_pi_gauss_legendre(int iterations) {
    double a = 1.0;
    double b = 1.0 / sqrt(2.0);
    double t = 0.25;
    double p = 1.0;
    double a_next;

    for (int i = 0; i < iterations; ++i) {
        a_next = (a + b) / 2.0;
        b = sqrt(a * b);
        t -= p * (a - a_next) * (a - a_next);
        a = a_next;
        p *= 2.0;
    }

    return ((a + b) * (a + b)) / (4.0 * t);
}
