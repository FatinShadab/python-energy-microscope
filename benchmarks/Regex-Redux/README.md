# Regex-Redux
The **Regex-Redux** is part of the **Computer Language Benchmarks Game (CLBG)**, designed to measure the performance of different programming languages in handling regular expressions and string processing tasks. It specifically deals with pattern matching and substitution in DNA sequences.

[Official CLBG Regex-Redux Page](https://benchmarksgame-team.pages.debian.net/benchmarksgame/description/regexredux.html)

## Algorithm

### Steps Involved
1. **Input Reading**: Read the DNA sequence from a FASTA format file and record the initial length.
2. **Sequence Cleaning**: Remove descriptions and line breaks using regular expressions and record the cleaned sequence length.
3. **Pattern Matching**: Count occurrences of DNA 8-mer patterns and their reverse complements.
4. **Pattern Substitution**: Sequentially apply a series of substitution patterns.
5. **Output Results**: Print the pattern counts and the sequence lengths.

### Patterns Used
- `agggtaaa|tttaccct`
- `[cgt]gggtaaa|tttaccc[acg]`
- `a[act]ggtaaa|tttacc[agt]t`
- `ag[act]gtaaa|tttac[agt]ct`
- `agg[act]taaa|ttta[agt]cct`
- `aggg[acg]aaa|ttt[cgt]ccct`
- `agggt[cgt]aa|tt[acg]accct`
- `agggta[cgt]a|t[acg]taccct`
- `agggtaa[cgt]|[acg]ttaccct`

### Substitution Patterns
- Replace `tHa[Nt]` with `<4>`
- Replace `aND|caN|Ha[DS]|WaS` with `<3>`
- Replace `a[NSt]|BY` with `<2>`
- Replace `<[^>]*>` with `|`
- Replace `\|[^|][^|]*\|` with `-`

## Time and Space Complexity

- **Time Complexity**: Dependent on the regular expression engine. Simple patterns can be processed in **O(n)** time, while complex patterns may require **O(n²)** due to backtracking.
- **Space Complexity**: **O(n)** where `n` is the size of the input DNA sequence.

## Pseudo Algorithm
```python
function regex_redux(file_path):
    # Step 1: Read input
    sequence = read_file(file_path)
    initial_length = length(sequence)

    # Step 2: Remove descriptions and line breaks
    sequence = regex_replace(">.*\n|\n", "", sequence)
    cleaned_length = length(sequence)

    # Step 3: Count pattern occurrences
    patterns = [
        'agggtaaa|tttaccct',
        '[cgt]gggtaaa|tttaccc[acg]',
        'a[act]ggtaaa|tttacc[agt]t',
        'ag[act]gtaaa|tttac[agt]ct',
        'agg[act]taaa|ttta[agt]cct',
        'aggg[acg]aaa|ttt[cgt]ccct',
        'agggt[cgt]aa|tt[acg]accct',
        'agggta[cgt]a|t[acg]taccct',
        'agggtaa[cgt]|[acg]ttaccct'
    ]

    for pattern in patterns:
        count = regex_count(pattern, sequence)
        print(pattern, count)

    # Step 4: Apply substitutions
    substitutions = [
        ('tHa[Nt]', '<4>'),
        ('aND|caN|Ha[DS]|WaS', '<3>'),
        ('a[NSt]|BY', '<2>'),
        ('<[^>]*>', '|'),
        ('\\|[^|][^|]*\\|', '-')
    ]

    for pattern, replacement in substitutions:
        sequence = regex_replace(pattern, replacement, sequence)

    # Step 5: Output final lengths
    substituted_length = length(sequence)

    print(initial_length)
    print(cleaned_length)
    print(substituted_length)
```

## Implementation Approach
- **Input Handling**: Efficiently read the entire FASTA file.
- **Regex Operations**: Use language-specific regex libraries for counting and substitution.
- **Optimized Looping**: Process patterns sequentially.
- **Output Handling**: Store and print results in the required format.


## References
1. [Regex-Redux Benchmark Description (CLBG)](https://benchmarksgame-team.pages.debian.net/benchmarksgame/description/regexredux.html)
2. Regular Expression Documentation (Python): https://docs.python.org/3/library/re.html
3. Computer Language Benchmark Game (CLBG): https://benchmarksgame-team.pages.debian.net

