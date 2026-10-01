/*pgm to store and display 5 subjects marks
for student*/    //((ctrl+/))==//(cmt will become===//)
#include<stdio.h>
int main(){
    int my_marks[5] = {0};      //int array size 5
    int sub_marks[5] = {0};    //declares an array 'sub marks' 
    //with SIZE 5 of 'int' type
    //storing data/ array initialization - array_name[index]=data/value;
    sub_marks[0]=80;  //stors '80' in a position whose index is '0'
    sub_marks[1]=78;
    sub_marks[2]=68;
    sub_marks[3]=58;
    sub_marks[4]=88;  //static array initialization
    //Fetch first array element from 'sub_marks' 
    printf ("First subject mark: %d",sub_marks[0]);
    //dynamic initialization of 'my_marks'

    for (int i=0;i<5;i++)
    {
     printf("enter %d subject marks:[int data]\n",i+1);
     scanf("%d",&my_marks[i]);
    }
    for (int i=0;i<5;i++){
        printf("Subject %d marks is: %d\n",i+1, my_marks[i]);
    }
    
    printf("enter first subject marks:[int data]");
    scanf("%d",&my_marks[0]);  //stored in first location
    printf("enter second subject marks:[int data]");
    scanf("%d",&my_marks[1]);  //stored in second location
    printf("enter third subject marks:[int data]");
    scanf("%d",&my_marks[2]);  //stored in third location
    printf("enter fourth subject marks:[int data]");
    scanf("%d",&my_marks[3]);  //stored in fourth location
    printf("enter fifth subject marks:[int data]");
    scanf("%d",&my_marks[4]);  //stored in fifth location
    printf("my sub1 mark:%d",my_marks[0]);
    printf("my sub2 mark:%d",my_marks[1]);
    printf("my sub3 mark:%d",my_marks[2]);
    printf("my sub4 mark:%d",my_marks[3]);
    printf("my sub5 mark:%d",my_marks[4]);


}