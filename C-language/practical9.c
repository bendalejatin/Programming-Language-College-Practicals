//Practical : 9- Write a program to generate the first N number of 
//Fibonacci series.The value of N is to be entered by the user.
//Enrollment No: 202203103510038
//Name : Jatin Bendale
//Branch : B.Tech. Computer Science and Engineering

#include<stdio.h>
void main()
{
    int i,x1=0,x2=1,x3,N;
    printf("Enter the value of N: ");
    scanf("%d",&N);

    for(i=1;i<=N;i++)
    {
        
        x3=x1+x2;
        printf("%d\t",x1);
        x1=x2;
        x2=x3;
    }

}