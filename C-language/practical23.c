// Enrollment No: 202203103510038
// Name : Jatin Bendale
// Branch : B.Tech. Computer Science and Engineering

#include<stdio.h>

void main()
{
    char my_str[10];
    int size;
    printf("Enter the string: ");
    gets(my_str);
    size = sizeof(my_str);
    for(int i=0;i<size;i++)
    {
        printf("%p --> %c\n",&my_str[i],my_str[i]);
    }
}