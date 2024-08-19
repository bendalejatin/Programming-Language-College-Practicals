//Practical : 11-  Write a program to print following patterns:
// 1
// 12
// 123
// 1234
// 12345
//
//     *
//    * *
//   * * *
//  * * * *
// * * * * *
//
// * * * * *
//  * * * *
//   * * *
//    * *
//     *
//
// ABCDE
// ABCD
// ABC
// AB
// A

#include<stdio.h>
void main()
{
    for (int i = 1; i <= 5; i++) // 1 to 5 lader
    {
        for (int j = 1; j <= i; j++)
        {
            printf("%d", j);
        }
        printf("\n");
    }
    printf("\n");
    for (int i = 5; i >= 1; i--) // pyramid
    {
        for (int j = 1; j < i; j++)
        {
            printf(" ");
        }
        for (int k = 1; k <= 6 - i; k++)
        {
            printf("* ");
        }
        printf("\n");
    }
    printf("\n");
    for (int i = 1; i <= 5; i++) // Inverse pyramid
    {
        for (int k = 1; k < i; k++)
        {
            printf(" ");
        }
        for (int j = 5; j >= i; j--)
        {
            printf("* ");
        }
        printf("\n");
    }
    printf("\n");
    for (char i = 'E'; i >= 'A'; i--) // ABCD pyramid
    {
        for (char j = 'A'; j <= i; j++)
        {
            printf("%c", j);
        }
        printf("\n");
    }
}
