#include <stdio.h>
#include <fcntl.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

void check_module(){
    char cmd[63];
    sprintf(cmd,"cat /proc/%d/maps | grep 'frida-agent.*so' | wc -l",(int)getpid());
    FILE* f;
    int n;
    f = popen(cmd,"r");
    fscanf(f,"%d",&n);
    if(n > 0) exit(0);
}
int main(void){
    FILE *f;
    char data[20];
    while(1){
        printf("Press any key to read file ...");
        getc(stdin);
        check_module();
        f = fopen("data","r+");
        fgets(data,19,f);
        printf("%s",data);
    }
}
