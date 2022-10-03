#include <stdio.h>
#include <stdlib.h>

int *fun(int *ptr1)
{
    *ptr1++ = 100;
    return ptr1;
}

int main(void)
{
    int a;
    int * ptr = &a;
    int * start = ptr;

    ptr = fun(ptr);
    while(1) {
        printf("%d\n",*start++);
    }
    return 0;
}