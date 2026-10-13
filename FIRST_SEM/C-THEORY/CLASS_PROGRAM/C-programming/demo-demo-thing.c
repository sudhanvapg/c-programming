#include <stdio.h>

int main(){

    int arraysize=read_array_size();
    int isvalid= validate_array_size(arraysize);
    while (isvalid==0)
    {
        int arraysize=read_array_size();
        int isvalid=validate_array_size(arraysize);
    }

}

int read_array_size(){
    int size;     //local variable
    printf("Enter the array size[>4]:");
    scanf("%d",&size);
    return size;
}

int validate_array_size(int array_size){
    if(array_size >4){
        return 1;
    }
    return 0;
