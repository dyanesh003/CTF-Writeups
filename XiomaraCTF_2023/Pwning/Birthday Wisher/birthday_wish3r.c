#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>

void getFlag()
{
    char flag[100];
    char *file = "/flag";
    int fd = open(file,O_RDONLY);
    if (fd < 0)
    {
        printf("Unable to open the file\n");
        return;
    }

    read(fd,&flag,100);
    printf("%s\n",flag);
    close(fd);
}

void getPresent()
{
    char input[100];
    int cont = 1;
    int n;
    printf("Enter the length of the name: ");
    scanf("%d",&n);
    printf("Enter the name of the person: ");
    read(0,input,n);
    printf("Happy Birthday %s\n",input);
    if (!strncmp(input,"root",4))
    {
        printf("If you are %s why are you here?\n",input);
    }
    else
    {
        printf("Sorry, there is no present available for %s\n",input);    
        printf("Want to wish for more people?   Enter 1 to continue: ");
        scanf("%d",&cont);
        printf("\n");
        if(cont == 1)
            getPresent();
    }
    
}

int main()
{
    setbuf(stdout, NULL);
    getPresent();
    return 0;
}
