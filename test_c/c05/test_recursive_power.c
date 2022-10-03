#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ft_recursive_power(int nb, int power);

int main(int argc, char *argv[])
{
    (void) argc;
    printf("%d", ft_recursive_power(atoi(argv[1]), atoi(argv[2])));
    return (0);
}
