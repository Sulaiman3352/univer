#include <math.h>
#include <stdio.h>    
#include <stdlib.h> 
#include <stdbool.h>
#include <time.h>

int main() {
    time_t t;
    int chances = 1;
    int A;
    srand((unsigned) time(&t));
    int ans = rand() % 1000 + 1;
   
    printf("Enter Your Guess: ");
    scanf("%d", &A);

    while (A != ans) {       
        
        if(A < ans){
            printf("Загадаанное число Болше \n");
        } else if (A > ans) {
            printf("Загадаанное число Меньше \n");
    }
    printf("Enter Your Guess: ");
    scanf("%d", &A);
     chances = chances+1;   
        
    }
    printf("угадали, ваш попыток: %d", chances);


    return 0;
}