def decrypt_test2(cipher):
    key = 'SYC'
    length = 18
    s2 = []
    for i in range(length):
        # 逆向计算 ord(s2[i])
        value = cipher[i] ^ i + ~ord(key[i % 3]) + 1
        # 确保 value 在 0 到 255 之间
        value &= 0xFF
        s2.append(chr(value))
    return ''.join(s2)

def decrypt_test(cipher, R):
    result = []
    for i in cipher:
        if 'A' <= i <= 'Z':
            result.append(chr((ord(i) - ord('A') - R) % 26 + ord('A')))
        elif 'a' <= i <= 'z':
            result.append(chr((ord(i) - ord('a') - R) % 26 + ord('a')))
        elif '0' <= i <= '9':
            result.append(chr((ord(i) - ord('0') - R) % 10 + ord('0')))
        else:
            result.append(i)
    return ''.join(result)

# 示例数据
num = [-1, -36, 26, -5, 14, 41, 6, -9, 60, 29, -28, 17, 21, 7, 35, 38, 26, 48]

# 解密 cipher2
cipher2 = num
s2 = decrypt_test2(cipher2)

# 解密 cipher1
a = 13
b = 14
c = a ^ (b + a)
d = b * 100
e = a ^ b
m = d * 4 - c + e - 1
r = m % 26
R = r 
cipher1 = decrypt_test(s2, R)

print("解密后的输入:", cipher1)