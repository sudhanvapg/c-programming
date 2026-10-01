#include <stdio.h>
int main (){
    int n;
    int total=0;
    int r=0;
    int p=0;
    int re=0;
    int c;
    int discount=0;
    printf("Enter number of tickets:");
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        printf("Enter category for ticket %d (1/2/3):",i+1);
        scanf("%d",&c);
        if (c==1){
            total+=150;
            r+=1;

        }
        else if (c==2) {
            total+=250;
            p+=1;
        }
        else if (c==3){
            total+=400;
            re+=1;
        }
        else{
            printf("Invalid category\n");

        }

    }
   
    printf("--- Final Bill ---\n");
    printf("Regular Tickets: %d\n", r);
    printf("Premium Tickets: %d\n",p);
    printf("Recliner Tickets: %d\n", re);
    printf("Total (before discount): %d\n", total);
    if (n>=5){
        discount=total*10/100;
        total=total-discount;
    }
    
    if (discount==0){
        printf("Discount applied: No\n");
    }
    else{
        printf("Discount applied: Yes\n");

    }
    printf("Final Amount: %d", total);
    return 0;

}