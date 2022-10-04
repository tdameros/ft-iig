#include <stdio.h>

int	ft_isalnum(int c);

int main(int argc, char **argv)
{
    (void) argc;

    printf("%d", ft_isalnum(argv[1][0]));
    return (0);
}
