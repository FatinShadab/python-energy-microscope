#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEN 1000

int max(int a, int b, int c, int d) {
    int max_val = a;
    if (b > max_val) max_val = b;
    if (c > max_val) max_val = c;
    if (d > max_val) max_val = d;
    return max_val;
}

int extend_alignment(
    const char *query,
    const char *target,
    int match,
    int mismatch,
    int gap,
    char *aligned_query,
    char *aligned_target
) {
    int n = strlen(query);
    int m = strlen(target);
    int dp[MAX_LEN][MAX_LEN] = {0};
    int max_score = 0, max_i = 0, max_j = 0;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            int score = (query[i - 1] == target[j - 1]) ? match : mismatch;
            dp[i][j] = max(
                0,
                dp[i - 1][j - 1] + score,
                dp[i - 1][j] + gap,
                dp[i][j - 1] + gap
            );
            if (dp[i][j] > max_score) {
                max_score = dp[i][j];
                max_i = i;
                max_j = j;
            }
        }
    }

    // Traceback
    int i = max_i, j = max_j;
    int ai = 0;
    while (i > 0 && j > 0 && dp[i][j] > 0) {
        int score = (query[i - 1] == target[j - 1]) ? match : mismatch;
        if (dp[i][j] == dp[i - 1][j - 1] + score) {
            aligned_query[ai] = query[i - 1];
            aligned_target[ai] = target[j - 1];
            i--; j--;
        } else if (dp[i][j] == dp[i - 1][j] + gap) {
            aligned_query[ai] = query[i - 1];
            aligned_target[ai] = '-';
            i--;
        } else {
            aligned_query[ai] = '-';
            aligned_target[ai] = target[j - 1];
            j--;
        }
        ai++;
    }

    aligned_query[ai] = '\0';
    aligned_target[ai] = '\0';

    // Reverse the aligned strings
    for (int k = 0; k < ai / 2; ++k) {
        char temp = aligned_query[k];
        aligned_query[k] = aligned_query[ai - 1 - k];
        aligned_query[ai - 1 - k] = temp;

        temp = aligned_target[k];
        aligned_target[k] = aligned_target[ai - 1 - k];
        aligned_target[ai - 1 - k] = temp;
    }

    return max_score;
}
