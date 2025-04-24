# cython: language_level=3, boundscheck=False, wraparound=False, cdivision=True

from libc.stdlib cimport malloc, free
from libc.string cimport memcpy
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef dict count_kmers(str sequence, int k):
    """
    Optimized k-mer counter using Cython with C-level buffers.
    """
    cdef int seq_len = len(sequence)
    cdef dict kmers = {}
    cdef int i, j
    cdef char* buffer = <char*> malloc((k + 1) * sizeof(char))
    cdef bytes kmer_b
    cdef str kmer

    if not buffer:
        raise MemoryError("Failed to allocate memory for k-mer buffer.")

    for i in range(seq_len - k + 1):
        for j in range(k):
            buffer[j] = sequence[i + j].encode('ascii')[0]
        buffer[k] = b'\0'[0]  # null terminate
        kmer_b = bytes(buffer[:k])
        kmer = kmer_b.decode('ascii')
        if kmer in kmers:
            kmers[kmer] += 1
        else:
            kmers[kmer] = 1

    free(buffer)
    return kmers
