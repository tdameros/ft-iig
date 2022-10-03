#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ft_strncmp(char *s1, char *s2, unsigned int n);

int main(int argc, char *argv[])
{
    (void) argc;
    int result = ft_strncmp(argv[1], argv[2], atoi(argv[3]));
    if (result < 0)
        printf("%d", -1);
    else if (result > 0)
        printf("%d", 1);
    else
        printf("%d", 0);
    return (0);
}