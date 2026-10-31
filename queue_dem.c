#include<stdio.h>
#include<stdbool.h>
#define i 5
int queue[i];
int front = -1,rear = -1;
int input(){
    int x;
    printf("1.Enqueue\n");
    printf("2.Dequeue\n");
    printf("3.Display queue\n");
    printf("4.Exit\n");
    printf("Enter your choice:");
    scanf("%d",&x);
    return x;
}

void dec(){
    printf("--------------\n");
}

void push(int temp,int front,int rear,int queue[]){
    if (rear == i - 1){
        printf("Queue is full:Overflow\n");
    } else {
        printf("Enter Data:");
        scanf("%d",&temp);
        front=0;
        queue[++rear] = temp;
        printf("%d pushed to rear %d of queue\n",temp,rear);
        temp = 0;
    }
}

void pull(int temp,int front,int rear,int queue[]){
    if ((front = -1) || (front > rear)){
     printf("Queue is Empty(underflow)\n");
     return;
    } else {
     temp = queue[front];
     printf("%d called from top of queue\n",temp);
     temp = 0;
    }
}

void display(int rear,int front,int queue[]){
    if (rear == -1 || front == -1){
        printf("Queue is empty\n");
    } else {
    printf("Queue:\n");
     for (int j = front;j >= rear;j--){
        printf("%d\n",queue[i]);
     }
    }
}

int main(void){
    int temp = 0,x;
    while (true) {
        x = input();
        if (x == 1)
        {
            push(temp,front,rear,queue);
        }
        else if (x == 2)
        {
            pull(temp,front,rear,queue);
        }
        else if (x == 3)
        {
            display(rear,front,queue);
        }
        else if (x == 4)
        {
            break;
        }
        else {
            printf("Enter Valid Choice.\n");
        }
        dec();
    }
}