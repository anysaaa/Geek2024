flag = 'SYC{MD5(input)}'

print('Please input0:')
input0 = input()

a = 13
b = 14
c = a ^ (b + a)
d = b * 100
e = a ^ b
m = d * 4 - c + e - 1
r = m % 26

def test2(s2):
    key = 'SYC'
    length = 18
    cipher = []
    for i in range(length):
        cipher.append(ord(s2[i]) ^ i + ~ord(key[i % 3]) + 1)
    return cipher

def test(s, R):
    result = []
    for i in s:
        if 'A' <= i <= 'Z':
            result.append(chr((ord(i) - ord('A') + R) % 26 + ord('A')))
        elif 'a' <= i <= 'z':
            result.append(chr((ord(i) - ord('a') + R) % 26 + ord('a')))
        elif '0' <= i <= '9':
            result.append(chr((ord(i) - ord('0') + R) % 10 + ord('0')))
        else:
            result.append(i)
    return ''.join(result)

cipher1 = test(input0, r)
cipher2 = test2(cipher1)

num = [-1, -36, 26, -5, 14, 41, 6, -9, 60, 29, -28, 17, 21, 7, 35, 38, 26, 48]

for i in range(18):
    if cipher2[i] != num[i]:
        print('wrong!')
        break
else:
    print('Rrrright!')