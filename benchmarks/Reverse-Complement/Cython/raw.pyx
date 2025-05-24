# cython: language_level=3
from libc.stdlib cimport malloc, free
from libc.string cimport memcpy
from cpython.bytes cimport PyBytes_FromStringAndSize

cdef unsigned char complement(unsigned char base):
    if base == b'A'[0]:
        return b'T'[0]
    elif base == b'T'[0]:
        return b'A'[0]
    elif base == b'C'[0]:
        return b'G'[0]
    elif base == b'G'[0]:
        return b'C'[0]
    else:
        return b'N'[0]  # Unknown base fallback

def reverse_complement(bytes dna_sequence):
    """
    Computes the reverse complement of a given DNA sequence.

    Args:
        dna_sequence (bytes): The input DNA sequence in bytes (e.g., b"ATGC").

    Returns:
        bytes: The reverse complement as bytes (e.g., b"GCAT").
    """
    cdef Py_ssize_t n = len(dna_sequence)
    cdef unsigned char* rev_comp = <unsigned char*>malloc(n)
    if not rev_comp:
        raise MemoryError("Failed to allocate memory")

    cdef Py_ssize_t i
    for i in range(n):
        rev_comp[i] = complement(dna_sequence[n - i - 1])

    result = PyBytes_FromStringAndSize(<char*>rev_comp, n)
    free(rev_comp)
    return result
