#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

#define rdtsc(t) asm("rdtsc;"           \
                     "shl $32,%%rdx;"   \
                     "or %%rax,%%rdx;"  \
                     "mov %%rax,%0;"    \
                     :"=r" (t)          \
                    );

unsigned long time1,time2;
int f (int n)
{
    rdtsc(time2);
    if( time2-time1 >= 3000){
        printf("What are you doing ?\n");
        exit(0);
    }
    return n++;
}

int main (int argc,char * argv[])
{
    int i = 0;
    printf ("f() berada di %p\n", f);
    while (1)
    {
        rdtsc(time1);
        printf("%d\n",f (i++));
        sleep (1);
    }
}
