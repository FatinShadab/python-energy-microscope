# Sieve of Eratosthenes 
The **Sieve of Eratosthenes** is an ancient algorithm used to find all prime numbers up to a specified integer `n`. It works by iteratively marking the multiples of each prime number starting from 2, the first prime number. The numbers that remain unmarked are prime.

This algorithm is widely used in number theory and is an efficient way to generate prime numbers for large values of `n`. Its time complexity is much better than checking each number for primality individually, making it especially useful for generating large lists of primes.

## Algorithm

1. **Input**: An integer `n`, where `n` is the upper limit up to which we want to find prime numbers.
2. **Output**: A list of all prime numbers less than or equal to `n`.

The algorithm proceeds as follows:
1. Create a list of boolean values, where each index represents whether the number is prime (True) or not (False).
2. Set the values at index 0 and 1 to False since 0 and 1 are not prime.
3. Iterate through the list starting from 2. For each prime number `p`, mark its multiples as non-prime.
4. After completing the iterations, the indices that have `True` values correspond to prime numbers.

## Pseudocode

```
function SieveOfEratosthenes(n):
    Initialize a boolean list sieve of size n+1, all values set to True
    Set sieve[0] and sieve[1] to False (since 0 and 1 are not prime)
    
    for i = 2 to sqrt(n):
        if sieve[i] is True:
            for j = i * i to n with step i:
                sieve[j] = False
    
    return [index for index, is_prime in enumerate(sieve) if is_prime]
```

## Implementation Approach

1. **Initialization**: We start by creating a list `sieve` where each index represents whether that number is prime. Initially, we assume all numbers are prime, except for 0 and 1, which are marked as False.
2. **Main Loop**: We loop from 2 up to the square root of `n`. If the current number is still marked as prime, we mark all of its multiples as non-prime (starting from `i*i` to avoid redundant work).
3. **Final Step**: After the loop finishes, all indices in the list that still have `True` values are prime numbers.
4. **Output**: We return a list of all indices corresponding to prime numbers.

## Time Complexity

The time complexity of the Sieve of Eratosthenes is **O(n log log n)**.
- For each number `p` from 2 to `sqrt(n)`, we mark its multiples, which requires iterating over a smaller subset of numbers each time.
- The summation of these operations results in a time complexity of **O(n log log n)**, which is efficient for generating primes up to large values of `n`.

## Space Complexity

The space complexity is **O(n)** due to the storage required for the sieve list of size `n+1`. This list stores a boolean value for each number from 0 to `n`, indicating whether the number is prime or not.

## Example Usage

```python
# Test the Sieve of Eratosthenes
n = 100
prime_numbers = PrimeSieve.sieve(n)
print(f"Prime numbers up to {n}: {prime_numbers}")
```

**Expected Output**:
```
Prime numbers up to 100: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

## References Used for Implementation and Information

1. **Wikipedia**: [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
2. **GeeksforGeeks**: [Sieve of Eratosthenes](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)
3. **Introduction to Algorithms** by Cormen, Leiserson, Rivest, and Stein: Provides a detailed explanation and analysis of the algorithm.