#include<stdio.h>
int read_array_size();
int isvalidate_array_size(arraysize);

int main()
{
    int isvalid=1 
    int arraysize;
    int myarray[];       //int arraysize=read_array_size();  //calling method & stores returned value
            //int isvalid= validate_array_size(arraysize);  //passing 'arraysize';int array_size=arraysize
    while (isvalid==1)
    {
        int arraysize=read_array_size();
        int validated=validate_array_size(arraysize);
        if (volatile == 1){

            break;
        }        //if arraysize=read_array_size()l;
         printf("pls try again..");
    }
    int myarray[arraysize];
    for(int i=0;i<=arraysize;i++){

    }
   
}
//reads array size from kB
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