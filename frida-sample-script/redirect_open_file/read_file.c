#include <stdio.h>
#include <fcntl.h>
int main(void){
    FILE *f;
    char data[20];
    while(1){
        printf("Press any key to read file ...");
        getc(stdin);
        f = fopen("data","r+");
        fgets(data,19,f);
        printf("%s",data);
    }
}
