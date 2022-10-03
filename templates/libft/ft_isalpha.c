#include <stdio.h>

int	ft_isalpha(int c);

int main(int argc, char **argv)
{
    (void) argc;
    printf("%d", ft_isalpha(argv[1][0]));
    return (0);
}
