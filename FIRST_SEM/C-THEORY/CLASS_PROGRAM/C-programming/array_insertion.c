//dynamic initialisation in loop 
#include<stdio.h>
intmain(){
    int numbers[5];
    int newdata;
    int index;
for(int i=0;i<4;i++){
    printf("input %d array element:",i+1);
    scanf("%d",&numbers[i]);
}
printf("enter the new element:");
scanf("%d",&newdata);
printf("enter index value:");
scanf("%d",&index);
   //insertion process to insert 'newdata' at index 'index'
    numbers[4]=numbers[3];
    numbers[3]=numbers[2];
    numbers[2]=newdata;
    for(int i=0;i<5;i++){
        printf("%d",numbers[i]);
    }


}  