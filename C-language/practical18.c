//Enrollment No: 202203103510038
//Name : Jatin Bendale
//Branch : B.Tech. Computer Science and Engineering

#include<stdio.h>
#include<string.h>

struct person
{
    char person_name[20];
    char date_of_joining[20];
    int salary;
};

void main()
{
    struct person p1;
    printf("Enter the person name: ");
    gets(p1.person_name);
    printf("Enter the person date of joining: ");
    gets(p1.date_of_joining);
    printf("Enter the person salary: ");
    scanf("%d",&p1.salary);

    printf("\n############Person Details############\n");
    printf("Person Name:%s \n",p1.person_name);
    printf("Person date of joining:%s \n",p1.date_of_joining);
    printf("Person salary:%d \n",p1.salary);
        
}