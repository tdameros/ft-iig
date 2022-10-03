#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void ft_putnbr_base(int nbr, char *base);

int main(int argc, char *argv[])
{
    (void) argc;
    ft_putnbr_base(atoi(argv[1]), argv[2]);
    return (0);
}
