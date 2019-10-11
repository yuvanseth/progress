include <cs50.h>
#include <stdio.h>
#include <string.h>

int main()
{
    int count = 0, i;
    char* main_string = get_string("Enter main string: ");
    char* sub_string = get_string("Enter string to be searched for: ");
    for (i = 0; i < strlen(main_string); i++)
    {
        int j = 0;
        if (main_string[i] == sub_string[j])
        {
           for ( ; j < strlen(sub_string); j++)
           {
              while (main_string[i] == sub_string[j])
              {
                  i++;
                  continue;
              }
           }
           count++;
        }
    }
    printf("The sub-string was found %d times\n", count);
}
