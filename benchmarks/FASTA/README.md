# FASTA

FASTA (Fast Alignment Search Tool) is an algorithm and program used for sequence comparison and alignment. It is primarily designed to search for local alignments between a query sequence and a target sequence (e.g., DNA, RNA, or protein sequences). The FASTA algorithm is widely used in bioinformatics for sequence similarity searching, such as comparing gene sequences or protein sequences in databases.

## FASTA Algorithm

The FASTA algorithm works by first identifying short, exact matching segments (called **k-tuples**) between the query and target sequences. These k-tuples are subsequences of length **k** that are common to both sequences. Once the k-tuples are identified, the algorithm extends these matches to find the best possible local alignment between the sequences, typically using dynamic programming techniques like **Smith-Waterman** or **Needleman-Wunsch**. The result is a high-scoring local alignment that identifies similar regions between the sequences.

## Implementation Approach of the FASTA Algorithm

1. **K-Tuple Search**: 
   - The FASTA algorithm starts by finding **k-length subsequences (k-tuples)** in the query and target sequences. This step involves sliding a window of size **k** across the sequences and extracting k-length substrings (or k-tuples).
   - These k-tuples are stored in a hash table or a dictionary, with the sequence as the key and the positions where it occurs in the target sequence as values.

2. **Matching k-Tuples**: 
   - The algorithm then searches for matches between k-tuples from the query sequence and those in the target sequence. Each match represents a potential region of interest for further extension.

3. **Extension**: 
   - For each k-tuple match found, the FASTA algorithm extends the match by comparing the surrounding bases (or amino acids in the case of protein sequences). This extension is often done using dynamic programming (e.g., Smith-Waterman for local alignment).
   - The extension continues as long as the alignment score improves or remains positive. The optimal local alignment is determined by a scoring scheme for matches, mismatches, and gaps.

4. **Scoring**: 
   - The alignment is scored based on a predefined scoring matrix (e.g., for nucleotide or protein sequences). A **match** might score positively, a **mismatch** negatively, and a **gap** may also be penalized.
   - The Smith-Waterman algorithm typically uses a **local alignment scoring scheme**, where the score is reset to zero if the score becomes negative, ensuring that only local regions with high similarity are aligned.

5. **Final Output**: 
   - After processing all potential k-tuple matches, the algorithm returns the best scoring local alignment, which may be a sub-region of the full query and target sequences.

## Time Complexity of FASTA

- The **k-tuple search** step involves extracting k-length subsequences from the query and target sequences. For sequences of length **N** (query) and **M** (target), this step takes **O(N * M)** time.
- The **extension step** involves performing local alignment (Smith-Waterman algorithm) for each k-tuple match. In the worst case, for each match, the time complexity of the dynamic programming extension is **O(N * M)**.
- Overall, the **time complexity** of the FASTA algorithm is **O(N * M)**, where **N** is the length of the query sequence and **M** is the length of the target sequence. This complexity is due to the combination of the k-tuple search and dynamic programming alignment extension.

## Space Complexity of FASTA

- The space complexity primarily arises from storing the k-tuples and the dynamic programming matrix.
- The **hash table** storing the k-tuples will require space proportional to the number of k-tuples and the length of the sequences, which is **O(N + M)**, depending on the size of the sequences and the number of k-tuple matches.
- The **dynamic programming matrix** used for alignment extension requires space of **O(N * M)**, as it stores the alignment scores for all possible subsequences of the query and target sequences.
- Therefore, the **space complexity** of the FASTA algorithm is **O(N * M)**.

## References Used for Implementation and Information

1. **Smith-Waterman Algorithm**: 
   - The extension phase of the FASTA algorithm relies on the **Smith-Waterman** algorithm, a well-known dynamic programming algorithm used for local sequence alignment. This method was described in:
     - **Smith, T. F., & Waterman, M. S. (1981).** "Identification of common molecular subsequences." *Journal of Molecular Biology*, 147(1), 195-197.
   - The algorithm is used for comparing two sequences by aligning them optimally over local regions.

2. **FASTA Algorithm**: 
   - The FASTA algorithm and its description can be found in:
     - **Pearson, W. R., & Lipman, D. J. (1988).** "Improved tools for biological sequence comparison." *Proceedings of the National Academy of Sciences*, 85(8), 2444-2448. DOI: [10.1073/pnas.85.8.2444](https://doi.org/10.1073/pnas.85.8.2444)
   - This paper introduced the FASTA algorithm for sequence comparison, which is widely used in bioinformatics.

3. **General Bioinformatics Textbooks**: 
   - A variety of bioinformatics textbooks cover sequence alignment techniques, including FASTA and its variants:
     - **Mount, D. W. (2004).** "Bioinformatics: Sequence and Genome Analysis." Cold Spring Harbor Laboratory Press.
     - **Durbin, R., Eddy, S. R., Krogh, A., & Mitchison, G. (1998).** "Biological Sequence Analysis: Probabilistic Models of Proteins and Nucleic Acids." Cambridge University Press.

## Summary

The FASTA algorithm is an efficient method for sequence alignment that starts by finding k-tuple matches between the query and target sequences. After identifying these matches, it extends them using dynamic programming to find the optimal local alignment. The algorithm has a time and space complexity of **O(N * M)**, making it suitable for comparing large sequences. This approach is widely used in bioinformatics tools like BLAST for similarity searching and sequence alignment.