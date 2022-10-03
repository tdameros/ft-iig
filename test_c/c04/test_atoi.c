#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ft_atoi(char *str);

int main(int argc, char *argv[])
{
    (void) argc;
    printf("%d", ft_atoi(argv[1]));
    return (0);
}
