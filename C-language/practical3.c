//Practical : 3- Write a C program to take temperature from the user 
//in Fahrenheit and display the temperature in Celsius.
//Enrollment No: 202203103510038
//Name : Jatin Bendale
//Branch : B.Tech. Computer Science and Engineering

#include<stdio.h>
void main()
{
  float Fehrenheit,Celcius ;

  printf("\nEnter the value of temperature in Fehrenheit: ");
  scanf("%f",&Fehrenheit) ;
 
  Celcius=(Fehrenheit-32) * 5/9 ;
  printf("\nThe value of temperature in Celcius:%.2f .\n",Celcius);

}