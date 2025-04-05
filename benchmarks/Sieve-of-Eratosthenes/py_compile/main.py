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


if __name__ == "__main__":
    n = 100000  # Example limit
    primes = PrimeSieve.sieve(n)
    print(f"Primes up to {n}: {primes}")