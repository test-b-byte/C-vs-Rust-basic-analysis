#include <stdio.h>



long long fibit(int n, int *opC) {
    if (n <= 2) { return 1; }
    long long n_1 = 1;
    long long n_2 = 1;
    for (int i = 3; i <= n; i++) {
        long long current = n_1 + n_2;
        (*opC)++;
        n_1 = n_2;
        n_2 = current;
    }
    return n_2;
}

int main() {
    int opC = 0;
    int passed = 0;
    if (fibit(1, &opC) == 1)                        { printf("test 1 passed\n"); passed++; }
    if (fibit(2, &opC) == 1)                        { printf("test 2 passed\n"); passed++; }
    if (fibit(7, &opC) == 13)                       { printf("test 3 passed\n"); passed++; }
    if (fibit(10, &opC) == 55)                      { printf("test 4 passed\n"); passed++; }
    if (fibit(20, &opC) == 6765)                    { printf("test 5 passed\n"); passed++; }
    if (fibit(93, &opC) == 12200160415121876738ULL) { printf("test 6 passed\n"); passed++; }
    printf("%d/6 tests passed.\n", passed);
    return 0;
}
