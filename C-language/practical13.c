//Practical : 13- Write a user defined function with a name swap() to 
//interchange the values of two variables, say x and y. Call your swap() 
//function from the main() function.

#include<stdio.h>
void swap(int x ,int y)
{
    int temp;
    temp=x;
    x=y;
    y=temp;
    printf("The value after swapping are x = %d and y = %d.\n",x,y);
}
void main()
{
    int x,y;
    printf("Enter the value of x:");
    scanf("%d",&x);
    printf("Enter the value of y:");
    scanf("%d",&y);

    swap(x,y);
}
