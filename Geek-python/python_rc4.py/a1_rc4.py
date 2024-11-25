def xor1(plaintext, xor_list):
    # 将字符串转换为整数列表
    try:
        xor_list = [ord(i) for i in xor_list]
    except:
        pass
    else:
        try:
            plaintext = [ord(i) for i in plaintext]
        except:
            pass
        else:
            for i in range(len(plaintext)):
                plaintext[i] ^= xor_list[i]
            return plaintext

def xor2(plaintext):
    try:
        plaintext = [ord(i) for i in plaintext]
    except:
        pass
    else:
        # 反向执行xor2操作
        for i in range(len(plaintext) - 2, -1, -1):  # 从倒数第二个元素开始
            plaintext[i + 1] ^= plaintext[i]
        return plaintext

def dec(ciphertext, key, xor_list):
    # 首先反转xor2操作
    ciphertext = xor2(ciphertext)
    # 然后反转xor1操作
    ciphertext = xor1(ciphertext, xor_list)
    # 最后使用RC4解密
    for i in ciphertext:
        print(i,end="")

# 示例使用
cipher = [158, 31, 205, 434, 354, 15, 383, 298, 304, 351, 465, 312, 261, 442,
 397, 474, 310, 397, 31, 21, 78, 67, 47, 133, 168, 48, 153, 99, 103,
 204, 137, 29, 22, 13, 228, 3, 136, 141, 248, 124, 26, 26, 65, 200,
 7]
key = "SYCFOREVER"
xor_list = list(range(len(cipher)))  # 使用密文长度创建XOR列表
dec(cipher, key, xor_list)
