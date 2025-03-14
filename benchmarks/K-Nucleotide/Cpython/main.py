import sys
from collections import defaultdict
from typing import Dict


def read_sequence(file_path: str) -> str:
    """Reads the DNA sequence from a file, ignoring headers.
    
    Args:
        file_path (str): Path to the input file containing the DNA sequence.
    
    Returns:
        str: The processed DNA sequence as a single string.
    """
    sequence: list[str] = []
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('>'):
                sequence.append(line.strip().upper())  # Convert to uppercase for consistency
    return ''.join(sequence)

def count_kmers(sequence: str, k: int) -> Dict[str, int]:
    """Counts the frequency of k-mers in the given DNA sequence.
    
    Args:
        sequence (str): The DNA sequence.
        k (int): Length of the k-mer.
    
    Returns:
        Dict[str, int]: A dictionary mapping k-mers to their frequencies.
    """
    kmers: Dict[str, int] = defaultdict(int)
    seq_len: int = len(sequence)
    
    for i in range(seq_len - k + 1):
        kmer: str = sequence[i:i + k]
        kmers[kmer] += 1
    
    return kmers

def print_kmer_frequencies(kmers: Dict[str, int]) -> None:
    """Prints k-mer frequencies sorted by frequency (descending), then alphabetically.
    
    Args:
        kmers (Dict[str, int]): Dictionary of k-mer counts.
    """
    sorted_kmers = sorted(kmers.items(), key=lambda item: (-item[1], item[0]))
    for kmer, freq in sorted_kmers:
        print(f"{kmer}: {freq}")

def main() -> None:
    """Main function to execute the K-Nucleotide frequency analysis."""
    if len(sys.argv) < 3:
        print("Usage: python k_nucleotide.py <file_path> <k>")
        return
    
    file_path: str = sys.argv[1]
    k: int = int(sys.argv[2])
    
    sequence: str = read_sequence(file_path)
    kmers: Dict[str, int] = count_kmers(sequence, k)
    print_kmer_frequencies(kmers)


if __name__ == "__main__":
    main()
