#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ft_find_next_prime(int nb);

int main(int argc, char *argv[])
{
    (void) argc;
    printf("%d", ft_find_next_prime(atoi(argv[1])));
    return (0);
}