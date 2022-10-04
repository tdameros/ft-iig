#include <stdio.h>
#include <stdlib.h>

int	ft_isascii(int c);

int main(int argc, char **argv)
{
    (void) argc;
    int nbr;

    nbr = atoi(argv[1]);
    printf("%d", ft_isascii(nbr));
    return (0);
}
