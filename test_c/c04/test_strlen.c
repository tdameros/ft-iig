
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ft_strlen(char *str);

int main(int argc, char *argv[])
{
    (void) argc;
    printf("%d", ft_strlen(argv[1]));
    return (0);
}
