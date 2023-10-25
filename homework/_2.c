#include <stdio.h>
#include <math.h>

int main() {
    const double t = 0.01;
    double x1, y1, r1, x2, y2, r2, d;
    
    printf("Введите координаты центра и радиус первой окружности:\n");
    scanf("%lf %lf %lf", &x1, &y1, &r1);
    
    printf("Введите координаты центра и радиус второй окружности:\n");
    scanf("%lf %lf %lf", &x2, &y2, &r2);
    
    d = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
    
    if (d > r1 + r2)
        printf("Окружности отделены");
    else if (fabs(d - (r1 + r2)) <= t)
        printf("Окружности соприкасаются");
    else if (d < r1 + r2) {
        if (d > r1 - r2)
            printf("Окружности пересекаются");
        else
            printf("Окружность внутри друг друга");
    }
    
    return 0;
}