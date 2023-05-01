#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void reverse_string(char *str) {
    size_t len = strlen(str);
    for (size_t i = 0; i < len / 2; i++) {
        char tmp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = tmp;
    }
}


int main()
{
    char flag[43];
    int ct[42] = {67, 74, 80, 95, 94, 68, 30, 91, 30, 75, 114, 95, 73, 114, 29, 29, 95, 65, 30, 114, 90, 114, 89, 69, 114, 89, 29, 29, 64, 30, 30, 28, 78, 76, 86, 122, 64, 76, 95, 117, 68, 66};

    printf("Enter the flag: ");
    scanf("%s", flag);

    if (strlen(flag) != 42) {
        printf("Keep Trying\n");
        exit(1);
    }

    char l[8][7] = {'\0'};
    for (int i = 0; i < strlen(flag); i += 6) {
        strncpy(l[i / 6], &flag[i], 6);
        reverse_string(l[i / 6]);
    }
    char nl[24][4] = {'\0'};
    int index = 0;
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 6; j += 3) {
            strncpy(nl[index], &l[i][j], 3);
            reverse_string(nl[index]);
            index++;
        }
    }

    char s[25] = {'\0'};
    for (int i = 23; i > 0; i-= 2) {
        strcat(s,nl[i-1]);
        strcat(s, nl[i]);
    }


    int nss[42] = {0};
    for (int i = 0; i < strlen(s); i++) {
        nss[i] = s[i] ^ 45;
    }

    if (memcmp(nss, ct, sizeof(ct)) == 0) {
        printf("Go Submit the Goddamn Flag!!!\n");
    } else {
        printf("Try Harder\n");
    }

    return 0;
}
