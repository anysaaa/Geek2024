#include <stdio.h>
#include <stdint.h>
#include <string.h>

int main() {
    uint8_t v8[256] = { 0 }, flag[256], hex_list[32];
    const char* key = "syclover";
    uint64_t result[] = {
        0xA67A02C9047D5B94,
        0x7EF9680DBC980739,
        0x7104F81698BFBD08,
        0x61DB8498B686155F
    };
    int v7 = 0, v6 = 0, i;
    for (i = 0; i < 256; i++) {
        v8[i] = key[i % 8];
        flag[i] = i;
    }
    for (i = 0; i < 256; i++) {
        v7 = (v8[i] + v7 + flag[i]) % 256;
        uint8_t temp = flag[i];
        flag [i] = flag[v7];
        flag[v7] = temp;
    }
    for (i = 0; i < 4; i++) {
        uint64_t num = result[i];
        for (int j = 0; j < 8; j++) {
            hex_list[i * 8 + j] = num & 0xFF;
            num >>= 8;
        }
    }
    v7 = 0;
    for (i = 0; i < 32; i++) {
        v6 = (v6 + 1) % 256;
        v7 = (v7 + flag[v6]) % 256;
        uint8_t temp = flag[v6];
        flag[v6] = flag[v7];
        flag[v7] = temp;
        hex_list[i] ^= flag[(flag[v6] + flag[v7]) % 256];
    }
    char decoded_flag[33];
    for (i = 0; i < 32; i++) {
        hex_list[i] ^= 0x14;
        decoded_flag[i] = hex_list[i];
    }
    decoded_flag[32] = '\0';
    printf("%s\n", decoded_flag);
    return 0;
}
