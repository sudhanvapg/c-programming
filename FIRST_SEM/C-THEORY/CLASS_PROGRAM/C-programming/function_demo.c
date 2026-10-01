#include <stdio.h>

void add_to_numbrt(int first,int second){   //function defination
    int sum;
    //int first=100;
    //[int second=200;
    sum=first+second; 
    printf("the sum is %d",sum);
}


int main(){
    add_to_numbrt(10,20);
    add_to_numbrt(100,200);
    printf("pgm terminated");
    return 0;
}