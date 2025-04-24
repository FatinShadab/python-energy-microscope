// kmer_counter.c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* kmer;
    int count;
} KmerCount;

typedef struct {
    KmerCount* data;
    int size;
    int capacity;
} KmerMap;

void init_map(KmerMap* map) {
    map->size = 0;
    map->capacity = 1024;
    map->data = (KmerCount*)malloc(map->capacity * sizeof(KmerCount));
}

void free_map(KmerMap* map) {
    for (int i = 0; i < map->size; ++i)
        free(map->data[i].kmer);
    free(map->data);
}

int find_index(KmerMap* map, const char* kmer) {
    for (int i = 0; i < map->size; ++i) {
        if (strcmp(map->data[i].kmer, kmer) == 0)
            return i;
    }
    return -1;
}

void insert_kmer(KmerMap* map, const char* kmer) {
    int idx = find_index(map, kmer);
    if (idx != -1) {
        map->data[idx].count += 1;
        return;
    }

    if (map->size == map->capacity) {
        map->capacity *= 2;
        map->data = (KmerCount*)realloc(map->data, map->capacity * sizeof(KmerCount));
    }

    map->data[map->size].kmer = strdup(kmer);
    map->data[map->size].count = 1;
    map->size += 1;
}

KmerMap* count_kmers(const char* sequence, int k) {
    int len = strlen(sequence);
    KmerMap* map = (KmerMap*)malloc(sizeof(KmerMap));
    init_map(map);

    char* buffer = (char*)malloc((k + 1) * sizeof(char));
    for (int i = 0; i <= len - k; ++i) {
        strncpy(buffer, sequence + i, k);
        buffer[k] = '\0';
        insert_kmer(map, buffer);
    }

    free(buffer);
    return map;
}
