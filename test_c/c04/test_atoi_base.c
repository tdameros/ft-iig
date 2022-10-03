
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ft_atoi_base(char *str, char *base);

int main(int argc, char *argv[])
{
    (void) argc;
    printf("%d", ft_atoi_base(argv[1], argv[2]));
    return (0);
}
