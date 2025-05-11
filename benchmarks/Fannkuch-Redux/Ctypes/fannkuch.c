// fannkuch.c
#include <stdio.h>

int count_flips(int perm[], int n) {
    int flips = 0;
    int perm_copy[20];
    for (int i = 0; i < n; ++i)
        perm_copy[i] = perm[i];

    int k = perm_copy[0];
    while (k != 1) {
        for (int i = 0, j = k - 1; i < j; ++i, --j) {
            int tmp = perm_copy[i];
            perm_copy[i] = perm_copy[j];
            perm_copy[j] = tmp;
        }
        flips++;
        k = perm_copy[0];
    }
    return flips;
}

int next_permutation(int perm[], int n) {
    int i = n - 2;
    while (i >= 0 && perm[i] >= perm[i + 1])
        --i;

    if (i < 0) return 0;

    int j = n - 1;
    while (perm[j] <= perm[i])
        --j;

    int tmp = perm[i];
    perm[i] = perm[j];
    perm[j] = tmp;

    for (int left = i + 1, right = n - 1; left < right; ++left, --right) {
        tmp = perm[left];
        perm[left] = perm[right];
        perm[right] = tmp;
    }

    return 1;
}

// Exposed to ctypes
void fannkuch_redux(int n, int* max_flips_out, int* count_max_flips_out) {
    int perm[20];
    for (int i = 0; i < n; ++i)
        perm[i] = i + 1;

    int max_flips = 0;
    int count_max_flips = 0;

    do {
        int flips = count_flips(perm, n);
        if (flips > max_flips) {
            max_flips = flips;
            count_max_flips = 1;
        } else if (flips == max_flips) {
            count_max_flips++;
        }
    } while (next_permutation(perm, n));

    *max_flips_out = max_flips;
    *count_max_flips_out = count_max_flips;
}
