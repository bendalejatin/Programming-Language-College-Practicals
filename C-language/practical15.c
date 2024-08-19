//Practical : 15- Write a C program to read and store the roll no and 
//marks of twenty students using an array. Display the same array to 
//user in appropriate format.
//Enrollment No: 202203103510038
//Name : Jatin Bendale
//Branch : B.Tech. Computer Science and Engineering

#include <stdio.h>
void main()
{
    long long int enrollment_no[20];
    int marks[20];
    
    for (int i = 0; i <20; i++)
    {   
        printf("Enter the Enrollment number:");
        scanf("%lld", &enrollment_no[i]);
        printf("Enter the marks:");
        scanf("%d", &marks[i]);
    }
    printf("Enrollment Number-->   Marks\n");
    for (int i = 0; i <20; i++)
    {   
        printf("%lld  -->   %d\n",enrollment_no[i],marks[i]);
    }
    
}