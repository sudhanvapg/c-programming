#include<stdio.h>
int main(){
    char name1[10];        //static inalisation
    for (int i =0; name1[i] != '\0'; i++){
        printf("name[%d] = %c\n ",i, name1[i]);
    }

 
    printf("[%.4s]");
}
