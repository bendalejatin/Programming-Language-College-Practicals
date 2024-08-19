//Enrollment No: 202203103510038
//Name : Jatin Bendale
//Branch : B.Tech. Computer Science and Engineering

#include <stdio.h>
#include<string.h>
void main()
{
    char str[100];
    int i;

    printf("Enter your text : ");
    gets(str);

    for(i=0; str[i]!='\0'; i++)
    {
        if(str[i]>='a' && str[i]<='z')
        {
            str[i] = str[i] - 32;
        }
    }

    printf("Uppercase string : %s \n",str);
}
