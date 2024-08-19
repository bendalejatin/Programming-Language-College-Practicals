//Practical : 5- Write a C program that scans an integer from the user 
//and checks whether the number is divisible by 5 or not.

#include<stdio.h>
void main()
{
  int a;

  printf("\nEnter the Number: ");
  scanf("%d",&a);

  if(a%5 == 0)
  {
    printf("The number is divisible by 5.\n");
  }
  else
  {
    printf("The number is not divisible by 5.\n");
  }
  
}
