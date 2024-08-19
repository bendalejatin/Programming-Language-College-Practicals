//Practical : 6- Write a C program to take the birth date as an 
//input and prints the current age of the user.
//Enrollment No: 202203103510038
//Name : Jatin Bendale
//Branch : B.Tech. Computer Science and Engineering

#include <stdio.h>
void main()
{
    int d1, m1, y1, d2, m2, y2, r1, r2, r3;

    printf("Enter your birth date: ");
    scanf("%d %d %d", &d1, &m1, &y1);
    printf("Enter the current date: ");
    scanf("%d %d %d", &d2, &m2, &y2);

    r3 = y2 - y1;
    if (d2 >= d1)
    {
        r1 = d2 - d1;
    }
    else
    {
        m2 = m2 - 1;
        d2 = d2 + 30;
        r1 = d2 - d1;
    }
    if (m2 >= m1)
    {
        r2 = m2 - m1;
    }
    else
    {
        y2 = y2 - 1;
        m2 = m2 + 12;
        r2 = m2 - m1;
    }
    printf("You have lived for %d years, %d months, %d days.\n", r3, r2, r1);
}