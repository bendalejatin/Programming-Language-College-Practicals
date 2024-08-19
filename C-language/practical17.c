//Practical : 17- Write a program to perform various string operations 
//on user entered string.

#include<stdio.h>
#include<string.h>
void main()
{
    char str1[20],str2[20];
    
    printf("Enter the String1:");
    scanf("%s",str1);
    printf("Enter the String2:");
    scanf("%s",str2);

    //To Demonstrate strcmp()
    int flag;
    flag = strcmp(str1,str2);
    if(flag == 0)
    {
        printf("\nString1 and String2 are same.\n");
    }
    else
    {
        printf("\nString1 and String2 are not same.\n");
    }
    printf("-------------------------------------------");
    
    //To Demonstrate strcasecmp()
    int case_flag;
    printf("\nString1:%s\n",str1);
    printf("String2:%s\n",str2);
    case_flag = strcasecmp(str1,str2);
    if(flag == 0)
    {
        printf("\nString1 and String2 are same.\n");
    }
    else
    {
        printf("\nString1 and String2 are not same.\n");
    }
    printf("-------------------------------------------");

    //To Demonstrate strlen()

    printf("\nString1:%s\n",str1);
    printf("String2:%s\n",str2);

    printf("The length of String1 is :%ld\n",strlen(str1));
    printf("The length of String2 is :%ld\n",strlen(str2));
    printf("-------------------------------------------");

    //To Demonstrate strcat()
    
    printf("\nString1:%s\n",str1);
    printf("String2:%s\n",str2);

    strcat(str1,str2);
    printf("%s\n",str1);
    printf("-------------------------------------------");

    //To Demonstrate strcpy()

    printf("\nString1:%s\n",str1);
    printf("String2:%s\n",str2);

    strcpy(str1,str2);
    printf("\nString1:%s\n",str1);
    printf("String2:%s\n",str2);
    printf("-------------------------------------------");

}
