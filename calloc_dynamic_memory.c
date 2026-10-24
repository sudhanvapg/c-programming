#include <stdio.h>
#include <stdlib.h>

int main(){
    int *p;
    p = (int *)calloc(5, sizeof(int));
    if (p == NULL){
        printf("Memory is not allocated\n");
        return 1;
    }
    printf("Address of allocated memory: %p\n", (void *)p);
    printf("Enter 5 integers:\n");
    for (int i = 0; i < 5; i++){
        scanf("%d", &p[i]);
    }
    printf("Display the integers:\n");
    for (int j = 0; j < 5; j++){
        printf("%d\n", p[j]);
    }
    free(p);
    p = NULL;
    printf("Memory has been freed successfully.\n");

    return 0;
}