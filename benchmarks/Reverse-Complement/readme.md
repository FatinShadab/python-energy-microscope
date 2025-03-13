# Reverse-Complement Algorithm

The **reverse-complement** of a DNA sequence is the sequence of nucleotides (base pairs) obtained by reversing the original sequence and replacing each nucleotide with its complementary counterpart. In DNA, the bases pair as:

- Adenine (A) pairs with Thymine (T)
- Cytosine (C) pairs with Guanine (G)
- Guanine (G) pairs with Cytosine (C)
- Thymine (T) pairs with Adenine (A)

For example, if the input DNA sequence is `5'-ATGC-3'`, its reverse-complement would be `5'-GCAT-3'`.

## Algorithm

1. **Input**: A DNA sequence string (e.g., "ATGC").
2. **Reverse**: Reverse the sequence (e.g., "ATGC" becomes "CGTA").
3. **Complement**: Replace each nucleotide with its complementary base:
    - A → T
    - T → A
    - C → G
    - G → C
4. **Output**: The reverse-complement of the input DNA sequence.

## Step-by-Step Algorithm

1. **Input**: A DNA sequence `S` of length `n`.
2. **Reverse the sequence**: Reverse the string `S` to get `S_reversed`.
3. **Complement the sequence**: Replace every character in `S_reversed` as follows:
   - Replace `A` with `T`
   - Replace `T` with `A`
   - Replace `C` with `G`
   - Replace `G` with `C`
4. **Output**: Return the modified string, which is the reverse-complement.

## Pseudocode

```text
Function ReverseComplement(DNA_sequence):
    reversed_sequence = reverse(DNA_sequence)          # Step 1: Reverse the sequence
    complement_sequence = ""                             # Initialize empty string for complement
    for base in reversed_sequence:                      # Step 2: Iterate through the reversed sequence
        if base == 'A':
            complement_sequence += 'T'
        else if base == 'T':
            complement_sequence += 'A'
        else if base == 'C':
            complement_sequence += 'G'
        else if base == 'G':
            complement_sequence += 'C'
    return complement_sequence                           # Step 3: Return the reverse-complement
```

## Implementation Approach

The process involves two main steps:
1. **Reversing** the input DNA sequence.
2. **Replacing** each nucleotide with its complementary nucleotide.

## Example

### Input:
```
ATGC
```

### Process:
1. Reverse: `CGTA`
2. Complement:
   - `C` → `G`
   - `G` → `C`
   - `T` → `A`
   - `A` → `T`

### Output:
```
GCAT
```

## Time Complexity

- **Reversing the string**: O(n), where `n` is the length of the input string.
- **Complementing the string**: O(n), because we need to iterate through each character and replace it with the complementary base.

Thus, the **total time complexity** is **O(n)**.

## Space Complexity

- The space complexity is O(n) because we are creating a new string of length `n` for the reversed and complemented sequence.

## References

1. **Biology Textbooks/Resources**: For understanding the biological context of DNA and base pairing.
2. **Wikipedia**: Information on [DNA sequencing](https://en.wikipedia.org/wiki/DNA_sequence) and [complementary base pairing](https://en.wikipedia.org/wiki/Base_pair).
3. **Programming Algorithms**: General string manipulation and sequence processing algorithms.