#include <stdio.h>
int rollno;      //global declaration
void getstudentdata(){
    printf("enter roll number");
    scanf("%d",&rollno);


void gettotal(){   
printf("Enter marks in 5 subjects:\n"); 
printf("Subject 1: "); 
scanf("%f", &marks1); 
printf("Subject 2: "); 
scanf("%f", &marks2); 
printf("Subject 3: "); 
scanf("%f", &marks3); 
printf("Subject 4: "); 
scanf("%f", &marks4); 
printf("Subject 5: "); 
scanf("%f", &marks5);
}

void gettotal(){
total = marks1 + marks2 + marks3 + marks4 + marks5; 
return sum;
}

float getaverage(){
average = total / 5;
return average ;  //return 'average' to main()reeee
}

void getcgpa(){
cgpa = average / 9.5; 

}

void getdisplay studentdetails(){
    printf("\n--- Student CGPA Report ---\n"); 
    printf("roll no: %d",rollno);
    printf("Total Marks: %.2f", total); 
    printf("Average: %.2f", average);
    printf("CGPA: %.2f", cgpa); 
    return 0; 
}     