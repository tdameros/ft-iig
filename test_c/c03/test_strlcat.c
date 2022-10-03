
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned int ft_strlcat(char *dest, char *src, unsigned int size);

int main(int argc, char *argv[])
{
    (void) argc;
    char dest[100];
    strcpy(dest, argv[1]);
    printf("%d\t%s", ft_strlcat(dest, argv[2], atoi(argv[3])), dest);
    return (0);
}