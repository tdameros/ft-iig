

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ft_is_prime(int nb);

int main(int argc, char *argv[])
{
    (void) argc;
    printf("%d", ft_is_prime(atoi(argv[1])));
    return (0);
}