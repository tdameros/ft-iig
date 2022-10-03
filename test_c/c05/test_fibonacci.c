#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ft_fibonacci(int index);

int main(int argc, char *argv[])
{
    (void) argc;
    printf("%d", ft_fibonacci(atoi(argv[1])));
    return (0);
}
