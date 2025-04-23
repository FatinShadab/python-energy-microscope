// prime_sieve.c
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

// Sieve function: returns dynamically allocated array of primes.
// Writes the number of primes into *prime_count.
int* sieve(int n, int* prime_count) {
    bool* is_prime = (bool*) malloc((n + 1) * sizeof(bool));
    if (!is_prime) return NULL;

    for (int i = 0; i <= n; i++)
        is_prime[i] = true;

    is_prime[0] = false;
    is_prime[1] = false;

    int sqrt_n = (int)sqrt((double)n);
    for (int i = 2; i <= sqrt_n; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i)
                is_prime[j] = false;
        }
    }

    // Count number of primes
    int count = 0;
    for (int i = 2; i <= n; i++) {
        if (is_prime[i]) count++;
    }

    // Allocate result array
    int* primes = (int*) malloc(count * sizeof(int));
    if (!primes) {
        free(is_prime);
        return NULL;
    }

    int idx = 0;
    for (int i = 2; i <= n; i++) {
        if (is_prime[i]) {
            primes[idx++] = i;
        }
    }

    free(is_prime);
    *prime_count = count;
    return primes;
}

// Free array created by sieve
void free_array(int* arr) {
    free(arr);
}
