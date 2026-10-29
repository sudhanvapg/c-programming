#include<stdio.h>
#include<stdlib.h>

int size = 5;
int stack[5];
int top = -1;

//method defination
void push(int newdata){
    if(top == size - 1){
        printf("stack is full, %d cannot be pushed\n", newdata);}
    else{
        top++;
        stack[top] = newdata;
        printf("%d is pushed to top of the stack \n", newdata);}
}
void pop(){
    if(top == -1){
        printf("stack is empty, nothing to pop\n");}
    else{
        printf("popped data:%d\n", stack[top]);
        top--;}
}
void display_stack(){
    int i;
    if(top == -1){
        printf("stack is empty\n");}
    else{
        printf("stack data (top to bottom):\n");
        for(i = top; i >= 0; i--){
            printf("%d\n", stack[i]);}
    }
}
int main(){
    int option, mydata;
    do{
        printf("1.push data\n");
        printf("2.pop data\n");
        printf("3.display stack\n");
        printf("4.exit\n");
        printf("enter your option:");
        scanf("%d", &option);
        switch(option){
            case 1:printf("enter the data:");
            scanf("%d", &mydata);
            push(mydata);
            break;
            case 2:pop();
            break;
            case 3:display_stack();
            break;
            case 4:exit(0);
            break;
            default:printf("invalid option\n");
        }
        printf("---------------------------------\n");
    }while(option < 4);
    return 0;
}