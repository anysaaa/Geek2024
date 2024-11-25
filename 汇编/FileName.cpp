#include <stdio.h>
int main() {
    char str[] = "TTDv^jrZu`Gg6tXfi+pZojpZSjXmbqbmt.&x";
    int length = sizeof(str) - 1;
    for (int i = 0; i < length; i += 2) {
        str[i] ^= 7;          
        str[i + 1] += 5;      
    }
    for (int i = 0; i < length; i++) {
        printf("%c", str[i]);
    }
    printf("\n");
    return 0;
}
