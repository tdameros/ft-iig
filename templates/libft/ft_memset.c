#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void *ft_memset(void *s, int c, size_t n);

int main(int argc, char **argv)
{
    int c;
    size_t n;
    if (argc == 5)
    {
        c = atoi(argv[3]);
        n = atoi(argv[4]);
        if (!strcmp(argv[1], "string"))
        {
            ft_memset(argv[2], c, n);
            printf("%s", argv[2]);
        } else if (!strcmp(argv[1], "int"))
        {
            int nbr = atoi(argv[2]);
            ft_memset(&nbr, c, n);
            printf("%d", nbr);
        } else if (!strcmp(argv[1], "float"))
        {
            float nbr = atof(argv[2]);
            ft_memset(&nbr, c, n);
            printf("%f", nbr);
        }
    }

    return (0);
}

