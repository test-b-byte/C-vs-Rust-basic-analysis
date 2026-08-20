#include <stdio.h>

long long fibrec(int n, long long *opC) {
    if (n <= 2) { return 1; }
    long long x = fibrec(n-1, opC) + fibrec(n-2, opC);
    (*opC)++;
    return x;
}

int main() {
    long long opC = 0;
    int passed = 0;
    if (fibrec(1, &opC) == 1)    { printf("test 1 passed\n"); passed++; }
    if (fibrec(2, &opC) == 1)    { printf("test 2 passed\n"); passed++; }
    if (fibrec(7, &opC) == 13)   { printf("test 3 passed\n"); passed++; }
    if (fibrec(10, &opC) == 55)  { printf("test 4 passed\n"); passed++; }
    if (fibrec(20, &opC) == 6765){ printf("test 5 passed\n"); passed++; }
    printf("%d/5 tests passed.\n", passed);
    return 0;
}
