#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main()
{

    int x = 707;
    int buf[128];

    scanf("%s",buf);
    
    if (x == 21012)
    {
        printf("You deserve this flag.\n");
        char flag[100];
        char *file = "/flag";
        int fd = open(file,O_RDONLY);
        if (fd < 0)
        {
            printf("Unable to open the file\n");
            return -1;
        }

        read(fd,&flag,100);
        printf("%s\n",flag);
        close(fd);
    }
    else
        printf("Nahh you lose\n");

    return 0;
    
}