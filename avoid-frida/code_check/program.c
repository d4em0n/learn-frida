#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
void f(int n){
    if( *(char*)f != 85) exit(0);
    printf("%d\n",n);
}

int main(void){
    int i = 0;
    printf("f() berada di %p\n", f);
    while(1){
        f(i++);
        sleep(1);
    }
}

