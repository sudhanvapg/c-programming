#include <stdio.h>

void swap(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int main()
{
    int m, n;

    printf("Enter two numbers: ");
    scanf("%d %d", &m, &n);

    swap(&m, &n);

    printf("After swapping: m = %d, n = %d", m, n);

    return 0;
}