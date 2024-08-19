//Practical : 7- Write a program to read student’s total marks as 
//input and program should display equivalent grade according 
//to following table:
// Marks =>Grades
// 100 - 80 =>Distinction
// 79-60 =>First Class
// 59 – 40 =>Second Class
// < 40 =>Fail

#include<stdio.h>
void main()
{
    int marks;

    printf("Enter your Total marks:");
    scanf("%d",&marks);

    if(marks<=100 && marks>=80)
    {
        printf("You got Distinction.\n");
    }
    else if(marks<=79 && marks>=60)
    {
        printf("You got First Class.\n");
    }
    else if(marks<=59 && marks>=40)
    {
        printf("You got Second Class.\n");
    }
    else
    {
        printf("Fail\n");
    }

}
