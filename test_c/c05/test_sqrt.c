#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ft_sqrt(int nb);

int main(int argc, char *argv[])
{
    (void) argc;
    printf("%d", ft_sqrt(atoi(argv[1])));
    return (0);
}