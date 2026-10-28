#include <stdio.h>  
#include <stdlib.h>

int main(){
    int *ptr; 
    int i; 
    int sum = 0;
    ptr = (int *)malloc(10 * sizeof(int)); 
    if (ptr == NULL){
        printf("Memory allocation failed.\n"); 
        return 1; 
    }
    printf("Enter 10 integers:\n"); 
    for (i = 0; i < 10; i++) {
        scanf("%d", &ptr[i]); 
        sum = sum + ptr[i]; 
    }
    printf("Sum of 10 integers = %d\n", sum); // Displays the total sum.
    free(ptr); 
    ptr = NULL; 

    return 0; 
}