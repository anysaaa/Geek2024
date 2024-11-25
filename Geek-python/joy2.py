from Crypto.Cipher import ARC4

flag = "43 BB BE 73 28 8E 42 D2 87 44 CA 99 37 33 E9 02 98 26 4C BE 23 F9 31 "
key = [int(i, 16) for i in flag.split()]

def initialize_s_box(key):
    key_length = len(key)
    s_box = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s_box[i] + key[i % key_length]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
    return s_box

def generate_key_stream(s_box, length):
    i = 0
    j = 0
    key_stream = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + s_box[i]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
        t = (s_box[i] + s_box[j]) % 256
        key_stream.append(s_box[t])
    return key_stream

def rc4_decrypt(ciphertext, key):
    s_box = initialize_s_box(key)
    key_stream = generate_key_stream(s_box, len(ciphertext))
    plaintext = bytearray([c ^ k for c, k in zip(ciphertext, key_stream)])
    return plaintext.decode('utf-8', errors='replace')

ciphertext_hex = "43 BB BE 73 28 8E 42 D2 87 44 CA 99 37 33 E9 02 98 26 4C BE 23 F9 31"
key = b"lovebeforeBC"

ciphertext = bytes.fromhex(ciphertext_hex)

# 解密
plaintext = rc4_decrypt(ciphertext, key)
print("解密后的明文:", plaintext)