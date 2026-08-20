#include <stdio.h>
#include <stdlib.h>
#include <time.h>



//Receives n(arg[1]) from terminal-main, iterates step by step to n-th term
//Operations counter present. Memo array is received, and space to count operations.
// if the calculation is made it deposits in into the index so it gets spotted next time around.

long long fibmem(int n, long long *memo, int *opC) {
    if(n <=2) {
        memo[n] = 1;
    }
    if (memo[n] != 0 || n == 0) {
        return memo[n];
    }
    // recursive portion
    memo[n] = fibmem(n-1, memo, opC) + fibmem(n -2, memo, opC);
    (*opC)++;
    return memo[n];
}


//calculates passes an int from terminal after program call to function. clock starts
// clock stops. prints each term from from 1 to n. stops clock. prints op number
int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    long long *memo = calloc(n +1, sizeof(int));
    int opC = 0;
    clock_t start, end;
    start = clock();
    for (int i = 1; i <= n; i++) {
        printf("term %d: %lld\n", i, fibmem(i, memo, &opC));
    }
    end = clock();
    double total = (double)(end-start) / CLOCKS_PER_SEC;
    free(memo);
    printf("Time: %fs\n", total);
    printf("Total Operations: %d\n", opC);
    return 0;
}