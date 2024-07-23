/* Doesn't work */

#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <string.h>

const int N = 50;

int main() {
    clock_t start, stop;
    start = clock();

    int iter, i, j, length, n;
    char *number = malloc(100 * sizeof(char));
    char *new_number = malloc(100 * sizeof(char));
    char *temp;
    char D;
    char suffix[] = {0, 0, 0};

    FILE *f = fopen("input.txt", "r");
    fgets(number, 100 * sizeof(char), f);
    fclose(f);

    
    for (iter = 1; iter <= N; ++iter) {
        printf("Iteration %d\n", iter);
        
        length = strlen(number);
        if (length > 50)
            /* Reallocate */
            temp = realloc(new_number, 2 * length * sizeof(int));
            if (temp == NULL) {
                free(number);
                free(new_number);
                return -999;
            }
            new_number = temp;

        i = 0;
        while (number[i] != '\0') {
            j = 0;
            D = number[i];
            n = 1;
            while(number[i + j] != '\0') {
                if (number[i + j + 1] == D) {
                    ++n;
                    ++j;
                }
                else
                    break;
            }
            suffix[0] = '0' + n;
            suffix[1] = D;
            strcat(new_number, suffix);
            i += n;
        }
        free(number);
        number = new_number;
    }


    free(number);
    free(new_number);
    stop = clock();
    printf("The time required for calculating term %d was %lf seconds", N, (double)(stop - start) / CLOCKS_PER_SEC);

    return 0;
}