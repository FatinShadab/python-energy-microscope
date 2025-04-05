def reverse_complement(dna_sequence: str) -> str:
    """
    Computes the reverse complement of a given DNA sequence.

    DNA bases are replaced with their complementary bases:
    - 'A' → 'T'
    - 'T' → 'A'
    - 'C' → 'G'
    - 'G' → 'C'

    The sequence is first reversed and then each base is replaced with its complement.

    Args:
        dna_sequence (str): The input DNA sequence (uppercase, consisting of A, T, C, G).

    Returns:
        str: The reverse complement of the input DNA sequence.
    
    Example:
        >>> reverse_complement("ATGC")
        'GCAT'
    """

    # Complement mapping dictionary
    complement_map: dict[str, str] = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    # Generate reverse complement using list comprehension (efficient in CPython)
    return "".join(complement_map[base] for base in reversed(dna_sequence))


if __name__ == "__main__":
    # Example DNA sequence
    dna = "ATGC"
    
    # Print results
    print("Original DNA Sequence: ", dna)
    print("Reverse Complement: ", reverse_complement(dna))
