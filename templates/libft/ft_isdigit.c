#include <stdio.h>

int	ft_isdigit(int c);

int main(int argc, char **argv)
{
    (void) argc;

    printf("%d", ft_isdigit(argv[1][0]));
    return (0);
}
