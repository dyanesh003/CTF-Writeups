#include <stdio.h>
#include <stdlib.h>

// char *flag = "Xiomara{xxx_sh0u1d_h4v3_3ncrypt3d_th3_f14g_xxx}";
long long p = 1056298169038583;

void collatz(char input[])
{
    int arr[] = {297, 517, 530, 287, 584, 468, 584, 556, 481, 481, 481, 491, 344, 318, 596, 313, 353, 305, 491, 318, 317, 282, 472, 491, 472, 331, 305, 468, 649, 256, 406, 472, 305, 491, 406, 318, 472, 491, 473, 353, 317, 455, 491, 481, 481, 481, 432};
    int i,n;
    unsigned long long tmp;
    char c = input[0];
    for(i = 0; i < 47; ++i)
    {
        n = 0;
        c = *(input+i);
        tmp = p*c;
        // printf("%c",c);
        while(tmp > 1)
        {
            if(tmp%2)
                tmp = 3*tmp+1;
            else
                tmp = tmp/2;
            ++n;
        }

        if (arr[i] != n)
        {
            printf("Can't trick me with a wrong flag\n");
            // printf("%c   %d\n",i,n);
            // printf("Quitting!!");
            return;
        }

    }

    printf("You got the flag!!!\n");
}

int main()
{
    char input[48];
    fgets(input,48,stdin);
    collatz(input);

    return 0;
    
}