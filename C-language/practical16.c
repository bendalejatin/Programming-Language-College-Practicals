//Practical : 16- Write a program to sort given array in ascending order using Bubble
// sort and Selection sort. 

// Selection sort
#include <stdio.h>
void main()
{
    int array[5], n, a, b, swap;
    printf("Enter number of elements\n");
    scanf("%d", &n);
    printf("Enter %d integers\n", n);
    for (a = 0; a < n; a++)
    {
        scanf("%d", &array[a]);
    }
    
    for (a = 0; a < n - 1; a++)
    {
        for (b = 0; b < n - a - 1; b++)
        {
            if (array[b] > array[b + 1])
            {

                swap = array[b];
                array[b] = array[b + 1];
                array[b + 1] = swap;
            }
        }
    }
    printf("Sorted list in ascending order:\n");
    for (a = 0; a < n; a++)
    {
        printf("%d\n", array[a]);
    }    
}

// Bubble sorting
#include <stdio.h>
void main()
{
    int i, j, count, temp, number[25];
    printf("How many numbers u are going to enter?: ");
    scanf("%d", &count);
    printf("Enter %d elements: ", count);
    for (i = 0; i < count; i++)
    {
        scanf("%d", &number[i]);
    }

    for (i = 0; i < count; i++)
    {
        for (j = i + 1; j < count; j++)
        {
            if (number[i] > number[j])
            {
                temp = number[i];
                number[i] = number[j];
                number[j] = temp;
            }
        }
    }
    printf("Sorted elements: ");
    for (i = 0; i < count; i++)
    {
        printf(" %d", number[i]);
    }
    
}
