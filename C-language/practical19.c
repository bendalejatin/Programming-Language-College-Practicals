//Enrollment No: 202203103510038
//Name : Jatin Bendale
//Branch : B.Tech. Computer Science and Engineering

#include<stdio.h>

struct cricket
{
    char Player_name[50];
    char Team_name[50];
    char Batting_average[5];
};

void main()
{
    struct cricket c1[5];
    printf("Enter the details of five players.\n");
    for (int i=1;i<=5;i++)
    {
        printf("Enter Name of Player %d:",i);
        gets(c1[i].Player_name);
        printf("Enter Team Name of Player %d:",i);
        gets(c1[i].Team_name);
        printf("Enter Batting Average of Player %d:",i);
        gets(c1[i].Batting_average);
    }
    printf("\n");
    for (int j=1;j<=5;j++)
    {
        puts(c1[j].Team_name);
        puts(c1[j].Player_name);
        puts(c1[j].Batting_average);
    }       
}