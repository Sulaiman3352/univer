#include <math.h>
#include <stdio.h>    
#include <stdlib.h> 
#include <iostream>
#include <cmath>


int main()
{

    int x1,y1,r1,x2,y2,r2,d;

    printf("Введите координаты центра и радиус первой окружности: ");
    scanf("%d %d %d", x1, y1, r1);

    printf("Введите координаты центра и радиус второй окружности:");
    scanf("%d %d %d", x2, y2, r2);

    d = sqrt(sqrt(x1-x2)+sqrt(y1-y2));
    if (d>r1+r2){

        printf("'Окружности отделены'");
    } else if (d-(r1+r2)) {
        printf("Окружности соприкасаются") ;  
    } else if (d<r1+r2) {
        if (d>r1-r2){
            printf("Окружности пересекаются");
        } else {
            printf("Окружность внутри друг друга");
        }   
    }


    return 0;
}