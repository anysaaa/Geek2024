key = "SYCLOVERSYCLOVER"
key = [ord(key[i]) for i in range(16)]
result = [0x99, 0xE8, 0xB8, 0x01, 0xC8, 0x82, 0x51, 0x93, 0x12, 0xEE, 0x89, 0x64, 0xE7, 0xEF, 0x63, 0x8D, 0x51, 0xDF, 0x5D, 0x78, 0x39, 0xAA, 0x39, 0x62, 0xA0, 0xB4, 0x50, 0x30, 0x47, 0x30, 0x21, 0x06]
ex_key = "LCYSREVOLCYSREVO"
ex_key = [ord(ex_key[i]) for i in range(16)]


def tea_1(temp,str):
    k = 0
    for i in range(4):
        for j in range(4):
            temp[4*j + i] = str[k]
            k += 1

def tea_2(temp,exkey):
    for i in range(4):
        for j in range(4):
            temp[i*4+j] ^= exkey[4*j + (3-i)]

def tea_3(temp,exkey):
    