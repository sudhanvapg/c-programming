#include<stdio.h>
int main(){
    int sumarray(int a[], int n)
    {
        if(n == 0)

        return a[n-1] + sumarray(a,n-1);
    }
}