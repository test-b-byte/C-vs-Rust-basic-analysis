#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//Receives n(arg[1]) from terminal-main, iterates step by step to n-th term
//Operations counter present

long long fibit(int n, int *opC) {
    if (n <= 2) {return 1;}
    long long n_1 = 1;
    long long n_2 = 1;
    for (int i = 2; i < n; i ++) {
        long long current =  n_1 + n_2;
        (*opC)++;
        n_1 = n_2;
        n_2 = current;
    }
    return n_2;
}

//calculates passes an int from terminal after program call to function. clock starts
// clock stops. prints each term from from 1 to n. stops clock. prints op number


int main(int argc, char *argv[]){ 
    int n = atoi(argv[1]);
    int opC = 0;
    clock_t start, end;
    start = clock();
    for (int i = 1; i <=n; i++) {
    printf("term %d: %lld\n", i, fibit(i, &opC));
    }
    end = clock();
    double total = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time: %fs\n", total);
    printf("Total Operations: %d\n", opC);
    return 0;
}
