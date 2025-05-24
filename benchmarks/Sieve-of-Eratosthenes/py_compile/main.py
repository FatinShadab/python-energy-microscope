import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

from typing import List


class PrimeSieve:
    """Class to find prime numbers using the Sieve of Eratosthenes algorithm."""
    
    @staticmethod
    def sieve(n: int) -> List[int]:
        """
        Finds all prime numbers up to `n` using the Sieve of Eratosthenes.
        
        Args:
            n (int): The upper limit to find primes up to.
        
        Returns:
            List[int]: A list of prime numbers up to `n`.
        """
        sieve = [True] * (n + 1)
        sieve[0], sieve[1] = False, False  # 0 and 1 are not prime
        
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        
        primes = [i for i, is_prime in enumerate(sieve) if is_prime]
        return primes

def main(n: int):
    """
    Main function to execute the sieve algorithm and print the results.
    
    Args:
        n (int): The upper limit to find primes up to.
    """
    primes = PrimeSieve.sieve(n)
    print(f"Primes up to {n}: {primes}")

@measure_energy_to_csv(n=__default__["sieve"]["test_n"], csv_filename="sieve_pycompile")
def run_energy_benchmark(n: int) -> None:
    main(n)

@measure_time_to_csv(n=__default__["sieve"]["test_n"], csv_filename="sieve_pycompile")
def run_time_benchmark(n: int) -> None:
    main(n)


if __name__ == "__main__":
    n = __default__["sieve"]["n"]
    
    run_energy_benchmark(n)
    run_time_benchmark(n)
