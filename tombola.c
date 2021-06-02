#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TABLE_LEN 90
#define K 3

void main(void) {
    int i, j, k, tmp_val, table_n[TABLE_LEN];
    time_t t;

    srand((unsigned)time(&t));

    for (i = 0; i < TABLE_LEN; i++)
        table_n[i] = i + 1;

    for (i = 0; i < TABLE_LEN * K; i++) {
        j = (double)rand() * TABLE_LEN / (RAND_MAX + 1);
        k = (double)rand() * TABLE_LEN / (RAND_MAX + 1);
        tmp_val = table_n[j];
        table_n[j] = table_n[k];
        table_n[k] = tmp_val;
    }

    for (i = 0; i < TABLE_LEN; i++)
        printf("%2d %2d %s\n", i + 1, table_n[i], table_n[i] == i + 1 ? "<*************" : "");
}