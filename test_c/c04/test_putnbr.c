#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void ft_putnbr(int nb);

int main(int argc, char *argv[])
{
    (void) argc;
    ft_putnbr(atoi(argv[1]));
    return (0);
}
