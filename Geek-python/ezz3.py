from z3 import *
s=Solver()
flag =[BitVec(('x%d'%i),8)for i in range(32)]
result = [0x0000019B, 0x00000113, 0x00000189, 0x000001C9, 0x00000250, 0x00000536, 0x000004DE, 0x000001BC, 0x0000041B, 0x00000724, 0x000006D0, 0x000004A1, 0x00000645, 0x00000475, 0x000004CA, 0x0000068C, 0x000003E5, 0x000001C7, 0x0000033D, 0x000005B7, 0x0000028D, 0x00000244, 0x0000030E, 0x00000291, 0x00000271, 0x00000301, 0x0000045F, 0x0000046F, 0x00000517, 0x0000041E, 0x00000426, 0x000004B5]


key = [0x2A, 0x0E, 0x0E, 0x14, 0x3F, 0x3F, 0x3F, 0x26, 0x11, 0x0A, 0x15, 0x15, 0x0E, 0x17, 0x10, 0x0E]

str = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?_"

for i in range(16):
    key[i] = str[key[i]]


def flag_change(flag):
    j = 0
    for i in range(7,-1,-1):
        while(1):
            if(j>=i):
                break
            else:
                flag[i+3],flag[i],flag[i+1],flag[i+2] = flag[i],flag[i+1],flag[i+2],flag[i+3]
                j+=1

#flag长度
#中间添加程序的加密正向算法
for i in range(0,32,4):
    s.add(flag[i] + 8 * flag[i+1] + 6 * flag[i+2] + flag[i+3] == result[i])
    s.add(flag[i+1] + 8 * flag[i+2] + 6 * flag[i+3] + flag[i] == result[i+1])
    s.add(flag[i+2] + 8 * flag[i+3] + 6 * flag[i] + flag[i+1] == result[i+2])
    s.add(flag[i+3] + 8 * flag[i] + 6 * flag[i+1] + flag[i+2] == result[i+3])

if s.check()==sat:
    model = s.model()
    flag  = [model[flag[i]].as_long().real for i in range(32)]
    for i in range(31,-1,-1):
        flag[i] = flag[i] ^ ord(key[(47-i)%16]) ^ i
        flag[i] = flag[i] ^ flag[(31 + i)%32]
    j = 0
    for i in range(7, -1, -1):
        while (1):
            if (j >= i):
                break
            else:
                flag[i + 3], flag[i], flag[i + 1], flag[i + 2] = flag[i], flag[i + 1], flag[i + 2], flag[i + 3]
                j += 1

    for i in flag:
        print(chr(i),end="")