//Practical : 14- Create a function that scan a character string passed as an argument and
// convert all lowercase character into their uppercase equivalents.

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
