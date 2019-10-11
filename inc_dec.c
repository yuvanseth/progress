#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string a = get_string("Enter your integer array: ");
    int i, count = 0;
    for (i = 0; i < strlen(a) - 1; i++)
    {
        if (a[i] <= a[i + 1])
            continue;
        else
            break;

    }
    for (int j = i; j < strlen(a) - 1; j++)
    {
        if (a[j] > a[j + 1])
            continue;
        else
        {
            printf("Not desired array\n");
            count++;
            break;
        }
    }
    if (count == 0)
            printf("Desired array!\n");
}
