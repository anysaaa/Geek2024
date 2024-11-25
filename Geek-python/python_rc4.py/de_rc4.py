cipher = [158, 31, 205, 434, 354, 15, 383, 298, 304, 351, 465, 312, 261, 442,
 397, 474, 310, 397, 31, 21, 78, 67, 47, 133, 168, 48, 153, 99, 103,
 204, 137, 29, 22, 13, 228, 3, 136, 141, 248, 124, 26, 26, 65, 200,
 7]
plaintext = [0] * 45
key = "SYCFOREVER"

for i in range(len(cipher)-1):
    cipher[i+1] = cipher[i] ^ cipher[i+1]
    
xor_list = list(range(len(cipher)))

for i in range(len(cipher)):
    cipher[i] ^= xor_list[i]

for i in range(len(cipher)):
    print(hex(cipher[i]),end="")