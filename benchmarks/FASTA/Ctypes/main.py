import ctypes
from ctypes import c_char_p, c_int, create_string_buffer

# Load the shared library
fasta_lib = ctypes.CDLL('./libfasta.so')

# Define the argument and return types
fasta_lib.extend_alignment.argtypes = [
    c_char_p, c_char_p, c_int, c_int, c_int,
    ctypes.c_char_p, ctypes.c_char_p
]
fasta_lib.extend_alignment.restype = c_int

def fasta_alignment_ctypes(query: str, target: str, match=1, mismatch=-1, gap=-2):
    aligned_q = create_string_buffer(1000)
    aligned_t = create_string_buffer(1000)

    score = fasta_lib.extend_alignment(
        query.encode('utf-8'),
        target.encode('utf-8'),
        match, mismatch, gap,
        aligned_q, aligned_t
    )

    return score, aligned_q.value.decode(), aligned_t.value.decode()

# Example usage
if __name__ == "__main__":
    query = "AGCTGACGTAG"
    target = "CGTAGAGCTGAC"

    score, aligned_q, aligned_t = fasta_alignment_ctypes(query, target)
    print("Best alignment score:", score)
    print("Aligned Query: ", aligned_q)
    print("Aligned Target:", aligned_t)
