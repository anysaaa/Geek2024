#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int caesar_decrypt(int ch, int shift) {
    if (ch >= '0' && ch <= '9') {
        return (ch - '0' - shift + 10) % 10 + '0'; 
    }
    else if (ch >= 'A' && ch <= 'Z') {
        return (ch - 'A' - shift + 26) % 26 + 'A'; 
    }
    else if (ch >= 'a' && ch <= 'z') {
        return (ch - 'a' - shift + 26) % 26 + 'a'; 
    }
    else {
        return ch;
    }
}
int main() {
    char key[] = "GEEK"; 
    char str[] = "0A161230300C2D0A2B303D2428233005242C2D26182206233E097F133A"; 
    int flag[32];  
    int len = strlen(str) / 2;
    for (int i = 0; i < len; i++) {
        sscanf(&str[i * 2], "%2X", &flag[i]);
    }

    for (int i = 0; i < len; i++) {
        flag[i] ^= key[i % 4]; 
    }
    int shift = 20;  
    for (int i = 0; i < len; i++) {
        flag[i] = caesar_decrypt(flag[i], shift); 
        printf("%c", flag[i]); 
    }
    printf("\n");

    return 0;
}
