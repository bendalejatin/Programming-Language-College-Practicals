//Practical : 20- Define a structure data type called time_ struct containing three
// member’s: integer hour,integer minute and integer second. Develop a
// program that would assign values to the individual number and display
// the time in the following format: 16:40:51

#include <stdio.h>

struct time_struct
{
    int hour;
    int minute;
    int second;
};

void main()
{
    struct time_struct t1;

    printf("Enter Current Hour: ");
    scanf("%d", &t1.hour);
    printf("Enter Current Minutes: ");
    scanf("%d", &t1.minute);
    printf("Enter Current Seconds: ");
    scanf("%d", &t1.second);

    printf("\nThe current time in HH:MM:SS format is- %d:%d:%d.\n",t1.hour,t1.minute,t1.second);
}
