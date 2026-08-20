#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* 
in this one operations had overflow, so this also 
needed to be converted to long*/
long long fibrec(int n, long long *opC) {
    if (n <= 2) { return 1; }
    long long x = fibrec(n-1, opC) + fibrec(n-2, opC);
    (*opC)++;
    return x;
}


//calculates passes an int from terminal after program call to function. clock starts
// clock stops. prints each term from from 1 to n. stops clock. prints op number
int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    long long opC = 0;
    clock_t start, end;
    start = clock();
    for (int i =1; i <= n; i++) {
        printf("term %d: %lld\n", i, fibrec(i, &opC));
    }
    end = clock();
    double total = (double)(end-start) / CLOCKS_PER_SEC;
    printf("Time: %fs\n", total);
    printf("Total Operations: %lld\n", opC);
    return 0;
}