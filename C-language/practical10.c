//Practical : 10- Write a program to find out the sum of the first 
//and last digit of a user entered number.
//Enrollment No: 202203103510038
//Name : Jatin Bendale
//Branch : B.Tech. Computer Science and Engineering

#include<stdio.h>
void main()
{
    int num,last_digit,Total;
    printf("Enter the number: ");
    scanf("%d",&num);

    last_digit= num%10;
    while(num>10)
    {
        num= num/10;
    }
    Total= num +last_digit;
    printf("The sum of first and last digit is %d.\n",Total);

}