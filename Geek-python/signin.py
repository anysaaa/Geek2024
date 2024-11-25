v8 = [0]*256
v7 = 0
flag = "syclover"
key = [i for i in range(256)]
for i in range(256):
    v8[i] = ord(flag[i%8])
for i in range(256):
    v7 = (v8[i] + v7 + key[i])%256
    key[i],key[v7]  = key[v7],key[i]
result= [
    0xA67A02C9047D5B94,
    0x7EF9680DBC980739,
    0x7104F81698BFBD08,
    0x61DB8498B686155F
]

hex_list = []
for num in result:
    hex_bytes = num.to_bytes(8, byteorder='little')
    hex_list.extend(hex_bytes)
v5,v6,v7 = 0,0,0
for i in range(32):
    v6 = (v6 + 1)%256 
    v7 = (v7 + key[v6])%256
    key[v6] ,key[v7] = key[v7],key[v6]
    hex_list[i] ^= key[(key[v6]+key[v7])%256]
flag = ""
for i in range(32):
    hex_list[i] ^= 0x14
    flag += chr(hex_list[i])
print(flag)
