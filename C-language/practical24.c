// Enrollment No: 202203103510038
// Name : Jatin Bendale
// Branch : B.Tech. Computer Science and Engineering

#include <stdio.h>
int main()
{
    int n;
    printf("Enter number of elements you want to sort: ");
    scanf("%d", &n);
    int a[n];
    int *p;
    p = a;
    for (int i = 0; i < n; i++)
    {

        printf("Enter element %d: ", i + 1);
        scanf("%d", &a[i]);
    }
    for (int j = 0; j < n; j++)
    {

        for (int i = 0; i < n - 1; i++)

        {

            if (*(p + i) > *(p + i + 1))

            {

                int temp;
                temp = *(p + i);
                *(p + i) = *(p + i + 1);
                *(p + i + 1) = temp;
            }
        }
    }
    printf("Sorted array is:\n");
    for (int i = 0; i < n; i++)
    {

        printf("%d ", a[i]);
    }
    printf("\n");
    return 0;
}