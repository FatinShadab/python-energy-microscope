// hanoi.c
// gcc -shared -o libhanoi.so -fPIC hanoi.c

#include <stdio.h>

void towers_of_hanoi(int n, const char* source, const char* auxiliary, const char* target) {
    if (n <= 0) {
        printf("Number of disks must be a positive integer.\n");
        return;
    }

    if (n == 1) {
        printf("Move disk 1 from %s to %s\n", source, target);
        return;
    }

    towers_of_hanoi(n - 1, source, target, auxiliary);
    printf("Move disk %d from %s to %s\n", n, source, target);
    towers_of_hanoi(n - 1, auxiliary, source, target);
}
