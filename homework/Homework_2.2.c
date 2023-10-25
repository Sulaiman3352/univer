#include <math.h>
#include <stdio.h>    
#include <stdlib.h> 
#include <stdbool.h>
#include <time.h>


int main() {
    time_t t;
    int num = 0;
    int chances = 1;
    char Myopration;
    char eqa = '=';

    printf("Enter the answer: ");
    scanf("%d", &num);
    bool S = false;
    srand((unsigned) time(&t));

    while (S == false) {
        printf("%d", rand() % 1000 + 1);

        printf(">, < or =: ");
        scanf("%c", &Myopration);

        if (Myopration == '=') {
                S = true;
                printf("угадали, ваш попыток: %d", chances);
            }
    chances = chances+1;  
    }
    return 0;
}