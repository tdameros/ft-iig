#include <stdio.h>
#include <stdlib.h>

int	ft_isprint(int c);

int main(int argc, char **argv)
{
    (void) argc;
    int nbr;

    nbr = atoi(argv[1]);
    printf("%d", ft_isprint(nbr));
    return (0);
}
