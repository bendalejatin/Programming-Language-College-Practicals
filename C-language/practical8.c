//Practical : 8- Write a C program to read numbers from 1 to 7 and 
//print respective day of the week to the user.
//Enrollment No: 202203103510038
//Name : Jatin Bendale
//Branch : B.Tech. Computer Science and Engineering

#include<stdio.h>
void main()
{
    int num;
    printf("Enter the number from 1 to 7: ");
    scanf("%d",&num);

    switch(num)
    {
        case 1:
        printf("Sunday\n");
        break;
        case 2:
        printf("Monday\n");
        break;
        case 3:
        printf("Tuesday\n");
        break;
        case 4:
        printf("Wednesday\n");
        break;
        case 5:
        printf("Thrusday\n");
        break;
        case 6:
        printf("Friday\n");
        break;
        case 7:
        printf("Saturday\n");
        break;
        default:
        {
            printf("Invalid Input\n");
        }       
    }
}