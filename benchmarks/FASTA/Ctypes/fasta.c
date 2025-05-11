#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LEN 1000

void generate_k_tuples(const char *seq, int k, char tuples[][MAX_LEN], int *positions, int *count) {
    int len = strlen(seq);
    *count = 0;
    for (int i = 0; i <= len - k; i++) {
        strncpy(tuples[*count], seq + i, k);
        tuples[*count][k] = '\0';
        positions[*count] = i;
        (*count)++;
    }
}

int extend_alignment(const char *query, const char *target, int match, int mismatch, int gap,
                     char *aligned_query, char *aligned_target) {
    int len_q = strlen(query);
    int len_t = strlen(target);
    int max_len = len_q > len_t ? len_q : len_t;
    
    int score = 0, i = 0;
    int a = 0;

    while (query[i] != '\0' && target[i] != '\0') {
        if (query[i] == target[i]) {
            aligned_query[a] = query[i];
            aligned_target[a] = target[i];
            score += match;
        } else {
            aligned_query[a] = query[i];
            aligned_target[a] = target[i];
            score += mismatch;
        }
        i++;
        a++;
    }

    // Remaining part: penalize gaps
    while (query[i] != '\0') {
        aligned_query[a] = query[i];
        aligned_target[a] = '-';
        score += gap;
        i++;
        a++;
    }

    while (target[i] != '\0') {
        aligned_query[a] = '-';
        aligned_target[a] = target[i];
        score += gap;
        i++;
        a++;
    }

    aligned_query[a] = '\0';
    aligned_target[a] = '\0';

    return score;
}

int fasta_alignment(const char *query, const char *target, int k,
                    int match, int mismatch, int gap,
                    char *best_aligned_query, char *best_aligned_target,
                    int *start_q, int *start_t) {
    char query_k_tuples[MAX_LEN][MAX_LEN];
    char target_k_tuples[MAX_LEN][MAX_LEN];
    int query_pos[MAX_LEN], target_pos[MAX_LEN];
    int query_count = 0, target_count = 0;

    generate_k_tuples(query, k, query_k_tuples, query_pos, &query_count);
    generate_k_tuples(target, k, target_k_tuples, target_pos, &target_count);

    int best_score = -999999;

    for (int i = 0; i < query_count; i++) {
        for (int j = 0; j < target_count; j++) {
            if (strcmp(query_k_tuples[i], target_k_tuples[j]) == 0) {
                char aligned_q[MAX_LEN];
                char aligned_t[MAX_LEN];

                int score = extend_alignment(query + query_pos[i], target + target_pos[j],
                                             match, mismatch, gap, aligned_q, aligned_t);

                if (score > best_score) {
                    best_score = score;
                    strcpy(best_aligned_query, aligned_q);
                    strcpy(best_aligned_target, aligned_t);
                    *start_q = query_pos[i];
                    *start_t = target_pos[j];
                }
            }
        }
    }

    return best_score;
}
