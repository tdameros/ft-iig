#include <stdio.h>

size_t    ft_strlen(const char *s);

int main(int argc, char **argv)
{
    (void) argc;

    printf("%zu", ft_strlen(argv[1]));
    return (0);
}
