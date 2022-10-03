#include <stdio.h>

int ft_strcmp(char *s1, char *s2);

int main(int argc, char *argv[])
{
    (void) argc;
    int result = ft_strcmp(argv[1], argv[2]);
    if (result < 0)
        printf("%d", -1);
    else if (result > 0)
        printf("%d", 1);
    else
        printf("%d", 0);
    return (0);
}