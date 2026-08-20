#include <stdio.h>
#include <stdlib.h>

long long fibmem(int n, long long *memo, int *opC) {
    if (n <= 2) { memo[n] = 1; return 1; }
    if (memo[n] != 0) { return memo[n]; }
    memo[n] = fibmem(n-1, memo, opC) + fibmem(n-2, memo, opC);
    (*opC)++;
    return memo[n];
}

int main() {
    int n = 93;
    long long *memo = calloc(n + 1, sizeof(long long));
    int opC = 0;
    int passed = 0;
    if (fibmem(1, memo, &opC) == 1)                        { printf("test 1 passed\n"); passed++; }
    if (fibmem(2, memo, &opC) == 1)                        { printf("test 2 passed\n"); passed++; }
    if (fibmem(7, memo, &opC) == 13)                       { printf("test 3 passed\n"); passed++; }
    if (fibmem(10, memo, &opC) == 55)                      { printf("test 4 passed\n"); passed++; }
    if (fibmem(20, memo, &opC) == 6765)                    { printf("test 5 passed\n"); passed++; }
    if (fibmem(93, memo, &opC) == 12200160415121876738ULL) { printf("test 6 passed\n"); passed++; }
    free(memo);
    printf("%d/6 tests passed.\n", passed);
    return 0;
}
