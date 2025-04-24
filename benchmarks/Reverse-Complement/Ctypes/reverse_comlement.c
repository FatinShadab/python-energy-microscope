#include <stdlib.h>
#include <string.h>

// Expose this function to Python
char* reverse_complement(const char* dna_sequence) {
    size_t n = strlen(dna_sequence);
    char* rev_comp = (char*) malloc(n + 1);

    if (!rev_comp) return NULL;

    for (size_t i = 0; i < n; ++i) {
        char base = dna_sequence[n - i - 1];
        switch (base) {
            case 'A': rev_comp[i] = 'T'; break;
            case 'T': rev_comp[i] = 'A'; break;
            case 'C': rev_comp[i] = 'G'; break;
            case 'G': rev_comp[i] = 'C'; break;
            default:  rev_comp[i] = 'N'; break;
        }
    }
    rev_comp[n] = '\0';
    return rev_comp;
}

// Free memory from Python side
void free_result(char* ptr) {
    free(ptr);
}
