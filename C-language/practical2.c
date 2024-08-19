//Practical : 2- Write a program to calculate the area of the circle and 
//volume of the cylinder. Use A = pi * r*r, V=pi * r*r*h.
//Use PI as a symbolic constant.

#include <stdio.h>
#define PI 3.14
void main()
{
    float a, r, v, h;
    printf("\n##########Area of the circle##########\n");

    printf("\nEnter the radius of the circle: ");
    scanf("%f", &r);

    a = PI * r * r;
    printf("\nThe Area of the circle is %.2f. \n", a);

    printf("\n######################################\n");

    printf("\n########Volume of the cylinder########\n");

    printf("\nEnter the radius of the cylinder: ");
    scanf("%f", &r);
    printf("Enter the height of the cylinder: ");
    scanf("%f", &h);

    v = PI * r * r * h;
    printf("\nThe Volume of the cylinder is %.2f. \n", v);

    printf("\n######################################\n");

    printf("\n#########Total surface area of the cylinder#########\n");

    printf("\nEnter the radius of the cylinder: ");
    scanf("%f", &r);
    printf("Enter the height of the cylinder: ");
    scanf("%f", &h);

    v = 2 * PI * r * (h + r);
    printf("\nThe Total surface area of the cylinder is %.2f. \n", v);

    printf("\n###################################################\n");
}
