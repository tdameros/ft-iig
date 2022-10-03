#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *ft_strcat(char *dest, char *src);

int main(int argc, char *argv[])
{
    (void) argc;
    char dest[100];
    strcpy(dest, argv[1]);
    printf("%s", ft_strcat(dest, argv[2]));
    return (0);
}