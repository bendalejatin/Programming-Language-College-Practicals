//Practical : 3- Write a C program to take temperature from the user 
//in Fahrenheit and display the temperature in Celsius.

#include<stdio.h>
void main()
{
  float Fehrenheit,Celcius ;

  printf("\nEnter the value of temperature in Fehrenheit: ");
  scanf("%f",&Fehrenheit) ;
 
  Celcius=(Fehrenheit-32) * 5/9 ;
  printf("\nThe value of temperature in Celcius:%.2f .\n",Celcius);

}
