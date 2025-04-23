# prime_sieve.pyx
from libc.math cimport sqrt
from cython cimport boundscheck, wraparound
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef list sieve(int n):
    """
    Finds all prime numbers up to `n` using the Sieve of Eratosthenes (optimized with Cython).
    
    Args:
        n (int): The upper limit to find primes up to.
    
    Returns:
        list: A list of prime numbers up to `n`.
    """
    cdef int i, j
    sieve = [True] * (n + 1)  # Regular Python list
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i in range(n + 1) if sieve[i]]

cpdef void driver(int n):
    """
    Main function to execute the sieve algorithm and print the results.
    
    Args:
        n (int): The upper limit to find primes up to.
    """
    primes = sieve(n)
    print(f"Primes up to {n}: {primes}")
