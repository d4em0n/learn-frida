#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void dummy();
int f (int n)
{
    if(__builtin_return_address(0) > (void*)dummy || __builtin_return_address(0) < (void*)f){
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
        printf("%d\n",f (i++));
        sleep (1);
    }
}
void dummy(){
    return;
}
