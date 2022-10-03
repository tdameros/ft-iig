#include <unistd.h>
#include <stdio.h>
#include <string.h>

void    ft_strcpy()
{
    char * toto = "toto";
    char * tutu = "tutu";
    strcpy(toto,tutu);
    printf(" toto est %s ", toto);
}