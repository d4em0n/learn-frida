#include <stdio.h>
#include <unistd.h>

void f(){
    printf("Hello world\n");
}
int main(void){
    printf("f() berada di %p\n",f);
    while(1){
        sleep(1);
        f();
    }
}
