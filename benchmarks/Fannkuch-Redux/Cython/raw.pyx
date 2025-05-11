# cython: boundscheck=False
# cython: wraparound=False

import numpy as np
cimport numpy as np

cpdef int count_flips(np.ndarray[np.int32_t, ndim=1] perm_view, int n):
    cdef np.ndarray[np.int32_t, ndim=1] perm = perm_view.copy()
    cdef int flips = 0
    cdef int first, i

    while True:
        first = perm[0]
        if first == 1:
            return flips
        # Flip the first `first` elements
        for i in range(first // 2):
            perm[i], perm[first - 1 - i] = perm[first - 1 - i], perm[i]
        flips += 1

cpdef bint next_permutation(np.ndarray[np.int32_t, ndim=1] perm, int n):
    cdef int i = n - 2
    cdef int j, tmp

    while i >= 0 and perm[i] > perm[i + 1]:
        i -= 1
    if i == -1:
        return False

    j = n - 1
    while perm[j] < perm[i]:
        j -= 1

    tmp = perm[i]
    perm[i] = perm[j]
    perm[j] = tmp

    # Reverse perm[i+1:]
    perm[i+1:] = perm[i+1:][::-1]
    return True

cpdef tuple fannkuch_redux(int n):
    cdef np.ndarray[np.int32_t, ndim=1] perm = np.arange(1, n + 1, dtype=np.int32)
    cdef int max_flips = 0
    cdef int count_max_flips = 0
    cdef int flips

    while True:
        flips = count_flips(perm, n)
        if flips > max_flips:
            max_flips = flips
            count_max_flips = 1
        elif flips == max_flips:
            count_max_flips += 1
        if not next_permutation(perm, n):
            break

    return max_flips, count_max_flips
