#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ft_recursive_factorial(int nb);

int main(int argc, char *argv[])
{
    (void) argc;
    printf("%d", ft_recursive_factorial(atoi(argv[1])));
    return (0);
}
