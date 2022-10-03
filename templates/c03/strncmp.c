#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    (void) argc;
    int result = strncmp(argv[1], argv[2], atoi(argv[3]));
    if (result < 0)
        printf("%d", -1);
    else if (result > 0)
        printf("%d", 1);
    else
        printf("%d", 0);
    return (0);
}