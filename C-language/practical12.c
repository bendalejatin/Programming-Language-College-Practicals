//Practical : 12- Write a program that defines a function to add 
//first N numbers. The value of N is to be entered by the user.

#include<stdio.h>

void sum_array(int my_nums[],int num_count)
{
    int sum = 0;
    for(int j=0;j<num_count;j++)
    {
        sum += my_nums[j];
    }
    printf("The summation of your numbers is %d. \n",sum);
}
void main()
{
    int num_count ,my_nums[100];
    printf("Enter the count of numbers: ");
    scanf("%d",&num_count);
    printf("Enter the numbers: ");
    for(int i=0;i<num_count;i++)
    {
        scanf("%d",&my_nums[i]);
    }
    sum_array(my_nums,num_count);
}
