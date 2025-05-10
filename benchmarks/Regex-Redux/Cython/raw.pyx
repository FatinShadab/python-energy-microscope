# distutils: language = c

from libc.stdio cimport fopen, fgets, fclose, FILE
import re

def read_fasta_file(str file_path) -> str:
    """
    Reads a FASTA file and returns a cleaned DNA sequence.
    """
    cdef FILE *file = fopen(file_path.encode('utf-8'), "r")
    if not file:
        raise IOError("File not found")

    cdef char line[4096]
    cdef list lines = []
    cdef str pyline

    while fgets(line, sizeof(line), file):
        pyline = line.decode('utf-8').strip()
        if not pyline.startswith('>'):
            lines.append(pyline.lower())  # Use Python .lower()

    fclose(file)
    return "".join(lines)

def count_patterns(str sequence, list patterns) -> list:
    """
    Counts occurrences of each regex pattern in the sequence.
    """
    cdef list results = []
    cdef str pattern
    cdef int count

    for pattern in patterns:
        count = len(re.findall(pattern, sequence))
        results.append((pattern, count))

    return results

def apply_substitutions(str sequence, list substitutions) -> str:
    """
    Applies a series of regex substitutions to the sequence.
    """
    cdef str pattern, repl
    for pattern, repl in substitutions:
        sequence = re.sub(pattern, repl, sequence)
    return sequence

def regex_redux(str file_path):
    """
    Main function to run the regex-redux benchmark.
    """
    sequence = read_fasta_file(file_path)
    initial_len = len(sequence)

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

    substitutions = [
        (r'tHa[Nt]', '<4>'),
        (r'aND|caN|Ha[DS]|WaS', '<3>'),
        (r'a[NSt]|BY', '<2>'),
        (r'<[^>]*>', '|'),
        (r'\|[^|][^|]*\|', '-')
    ]

    print("Pattern Counts:")
    for pattern, count in count_patterns(sequence, patterns):
        print(f"{pattern}: {count}")

    modified_sequence = apply_substitutions(sequence, substitutions)

    print("\nInitial Length:", initial_len)
    print("Cleaned Length:", len(sequence))
    print("Substituted Length:", len(modified_sequence))
