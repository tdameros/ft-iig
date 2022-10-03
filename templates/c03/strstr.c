#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    (void) argc;
    printf("%s", strstr(argv[1], argv[2]));
    return (0);
}
