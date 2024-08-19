//Practical : 21- Write a C program to print the address of a variable using a pointer.

#include<stdio.h>

void main()
{
    int x=5;
    int *my_ptr;
    my_ptr=&x;

    printf("The value of x: %d\n", x);
    printf("The value of *my_ptr: %d\n",*my_ptr);
    printf("The address of x: %p\n",my_ptr);
}
