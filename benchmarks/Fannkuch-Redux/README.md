# Fannkuch-Redux Algorithm

The **Fannkuch-Redux** problem is a computational problem often used as a benchmark in algorithmic performance tests. It involves generating permutations of a list of integers and calculating the number of flips required to transform each permutation into the sorted list. The goal is to compute the maximum number of flips encountered and the count of permutations that result in that maximum.

This problem is a variation of the classic **Fannkuch** problem and is part of the **Computer Language Benchmarks Game (CLBG)**.

## Problem Description

Given a list of integers from 1 to `n`, the task is to generate all permutations of the list, apply a "flip" operation on each permutation, and determine how many flips are needed to return the list to its sorted form. The algorithm must track the maximum number of flips encountered and how many times this maximum occurs across all permutations.

### Flip Operation

A **flip** operation on a permutation is defined as:
1. Find the largest element in the list (ignoring the first element).
2. Reverse the portion of the list that starts from the second element up to the largest element.
3. Count each such operation as a flip.

## Algorithm

### Steps:
1. **Permute the list**: Generate all permutations of the given list of integers.
2. **Calculate flips**: For each permutation, determine how many flips are required to transform the permutation into the identity permutation (sorted list).
3. **Repeat**: Apply the above steps to multiple permutations and find the one with the maximum flips.
4. **Result**: Output the maximum number of flips and the number of occurrences of that maximum.

## Time Complexity:
- Generating all permutations of a list of size `n` takes \(O(n!)\) time, as there are `n!` possible permutations.
- Calculating the flips for each permutation takes \(O(n)\) time, making the overall complexity \(O(n \cdot n!)\).

## Space Complexity:
- The space complexity is dominated by the need to store all permutations, which requires \(O(n!)\) space.

## Pseudocode

```text
1. Initialize variables:
   - max_flips = 0
   - count_max_flips = 0
   - perm = [1, 2, ..., n]  // Initial permutation
   - perm_count = [0] * n   // To store flip counts for each permutation

2. Function to calculate flips for a given permutation:
   - flips = 0
   - while True:
       - first = perm[0]
       - if first == 1:
           - return flips
       - perm[1:first] = reverse(perm[1:first])  // Reverse the segment of the list
       - flips += 1

3. Main logic to find the maximum flips:
   - perm = [1, 2, ..., n]  // Initialize the permutation array
   - Repeat for all permutations:
       - flips = count_flips(perm)
       - if flips > max_flips:
           - max_flips = flips
           - count_max_flips = 1
       - else if flips == max_flips:
           - count_max_flips += 1
       
       - Generate the next permutation

4. Return Result:
   - return max_flips, count_max_flips

5. Helper function to generate the next permutation:
   - i = n - 2
   - while i >= 0 and perm[i] > perm[i + 1]:
       - i -= 1
   - if i == -1:
       - return False
   - j = n - 1
   - while perm[j] < perm[i]:
       - j -= 1
   - swap(perm[i], perm[j])
   - reverse(perm[i + 1:])
   - return True
```

## Example

### Input:
The input is a single integer `n`, the size of the list of integers.

```text
n = 5
```

### Output:
The output consists of two values:
- The maximum number of flips encountered.
- The count of permutations that resulted in that maximum number of flips.

```text
Max flips: 4
Count of max flips: 12
```

**Explanation**:  
For `n = 5`, there are multiple permutations, and the maximum number of flips required is 4. This maximum occurred in 12 different permutations.

## Implementation Approach

1. **Generate Permutations**: Use a standard permutation generation algorithm like Heap's algorithm or Steinhaus-Johnson-Trotter.
2. **Flip Calculation**: For each permutation, calculate the number of flips required to transform it into the identity permutation (sorted list).
3. **Track Maximum Flips**: Track the highest number of flips and the number of permutations that result in that maximum.
4. **Efficient Memory Usage**: Use in-place operations to generate permutations and calculate flips, optimizing space complexity.

## References

- **Fannkuch-Redux on Wikipedia**: [Link to Wikipedia](https://en.wikipedia.org/wiki/Fannkuch)
- **Computer Language Benchmarks Game**: [Link to CLBG](https://benchmarksgame-team.pages.debian.net/benchmarksgame/)

## Conclusion

The **Fannkuch-Redux** problem is an interesting computational challenge that involves working with permutations and flip operations. Its time complexity grows rapidly with the size of `n`, making it an excellent benchmark for testing computational power and optimization techniques.
