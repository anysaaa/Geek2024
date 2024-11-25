def decrypt_test2(cipher):
    key = 'SYC'
    length = 18
    original = []
    for i in range(length):
        char = ord(cipher[i]) - 1
        char = char ^ ord(key[i % 3])
        char = char ^ i
        original.append(chr(char & 0xFF))  # 确保结果在 0 到 255 之间
    return ''.join(original)

def decrypt_test(s):
    R = 13  # 使用相同的偏移量
    result = []
    for i in s:
        if 'A' <= i <= 'Z':
            result.append(chr(((ord(i) - ord('A') - R + 26) % 26) + ord('A')))
        elif 'a' <= i <= 'z':
            result.append(chr(((ord(i) - ord('a') - R + 26) % 26) + ord('a')))
        elif '0' <= i <= '9':
            result.append(chr(((ord(i) - ord('0') - R + 10) % 10) + ord('0')))
        else:
            result.append(i)
    return ''.join(result)

# 给定的 num 数组
num = [-1, -36, 26, -5, 14, 41, 6, -9, 60, 29, -28, 17, 21, 7, 35, 38, 26, 48]

# 构造 cipher2
cipher2 = [chr((n + 1) & 0xFF) for n in num]

# 打印中间结果，确保每个字符都是有效的
print("Cipher2:", cipher2)

# 解密 cipher2 得到 cipher1
cipher1 = decrypt_test2(cipher2)

# 从 cipher1 中去掉末尾的 r 值，并解密得到原始输入
# 注意，这里假设 r 是一个两位数，因此去掉最后两位
original_input = decrypt_test(cipher1[:-2])

print(original_input)