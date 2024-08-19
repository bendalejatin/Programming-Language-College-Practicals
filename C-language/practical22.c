// Enrollment No: 202203103510038
// Name : Jatin Bendale
// Branch : B.Tech. Computer Science and Engineering

#include<stdio.h>
void swap(int *x ,int *y)
{
    int temp;
    temp=*x;
    *x=*y;
    *y=temp;
    }
void main()
{
    int x,y;
    printf("Enter the value of x:");
    scanf("%d",&x);
    printf("Enter the value of y:");
    scanf("%d",&y);
    printf("The value before swapping are x = %d and y = %d.\n",x,y);
    swap(&x,&y);
    printf("The value after swapping are x = %d and y = %d.\n",x,y);
}