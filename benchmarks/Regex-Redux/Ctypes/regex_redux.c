#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <regex.h>
#include <ctype.h>

// Reads the input file and returns a dynamically allocated string (no line breaks or headers)
char* read_fasta_file(const char* filename, int* out_length) {
    FILE* file = fopen(filename, "r");
    if (!file) return NULL;

    fseek(file, 0, SEEK_END);
    long size = ftell(file);
    rewind(file);

    char* buffer = malloc(size + 1);
    fread(buffer, 1, size, file);
    buffer[size] = '\0';
    fclose(file);

    // Strip headers (lines starting with '>') and newlines
    char* cleaned = malloc(size + 1);
    int j = 0;
    int in_header = 0;

    for (long i = 0; i < size; ++i) {
        if (buffer[i] == '>') {
            in_header = 1;
        } else if (buffer[i] == '\n') {
            in_header = 0;
        } else if (!in_header) {
            cleaned[j++] = tolower(buffer[i]);
        }
    }
    cleaned[j] = '\0';
    free(buffer);

    *out_length = j;
    return cleaned;
}

// Count pattern matches
int count_pattern(const char* sequence, const char* pattern) {
    regex_t regex;
    regmatch_t match;
    int count = 0;

    if (regcomp(&regex, pattern, REG_EXTENDED | REG_ICASE) != 0) {
        return -1;
    }

    const char* cursor = sequence;
    while (regexec(&regex, cursor, 1, &match, 0) == 0) {
        count++;
        cursor += match.rm_eo;
    }

    regfree(&regex);
    return count;
}

// Exported C function for Python
__attribute__((visibility("default")))
void regex_redux(const char* filename) {
    int original_len;
    char* sequence = read_fasta_file(filename, &original_len);

    if (!sequence) {
        printf("Failed to read file.\n");
        return;
    }

    const char* patterns[] = {
        "agggtaaa|tttaccct",
        "[cgt]gggtaaa|tttaccc[acg]",
        "a[act]ggtaaa|tttacc[agt]t",
        "ag[act]gtaaa|tttac[agt]ct",
        "agg[act]taaa|ttta[agt]cct",
        "aggg[acg]aaa|ttt[cgt]ccct",
        "agggt[cgt]aa|tt[acg]accct",
        "agggta[cgt]a|t[acg]taccct",
        "agggtaa[cgt]|[acg]ttaccct"
    };

    printf("Pattern Counts:\n");
    for (int i = 0; i < 9; ++i) {
        int count = count_pattern(sequence, patterns[i]);
        printf("%s: %d\n", patterns[i], count);
    }

    printf("\nInitial Length: %d\n", original_len);
    printf("Cleaned Length: %ld\n", strlen(sequence));
    // Skipping substitutions in this C version for now

    free(sequence);
}