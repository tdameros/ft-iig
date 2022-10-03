#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    (void) argc;
    int result = strcmp(argv[1], argv[2]);
    if (result < 0)
        printf("%d", -1);
    else if (result > 0)
        printf("%d", 1);
    else
        printf("%d", 0);
    return (0);
}