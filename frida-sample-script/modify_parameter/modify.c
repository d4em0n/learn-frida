#include <stdio.h>
#include <unistd.h>

void f(int n){
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

