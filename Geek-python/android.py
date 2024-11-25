import binascii

def hex_string_to_32bit_int_array(hex_str):
    # 将十六进制字符串转换为字节对象
    byte_data = binascii.unhexlify(hex_str)
    
    # 确保字节对象的长度是4的倍数
    if len(byte_data) % 4 != 0:
        raise ValueError("Hex string length must be a multiple of 8 characters")
    
    # 将字节对象每4个字节分割，并转换为32位整数
    int_array = [int.from_bytes(byte_data[i:i+4], byteorder='little') for i in range(0, len(byte_data), 4)]
    
    return int_array
def int_array_to_hex8_array(int_array):
    # 将每个32位整数转换成8位的十六进制字符串
    hex8_array = []
    for value in int_array:
        # 确保值为非负数
        value &= 0xFFFFFFFF
        # 将32位整数转换为4个字节的字节对象（使用小端序）
        bytes_obj = value.to_bytes(4, byteorder='little')
        # 将每个字节转换为2位的十六进制字符串
        for i in range(4):
            hex8_array.append(bytes_obj[i].to_bytes(1, byteorder='big').hex())
    
    return hex8_array


def hex8_array_to_ascii(hex8_array):
    # 将8位的十六进制字符串数组转换成ASCII码
    ascii_str = ""
    for hex_str in hex8_array:
        byte_value = int(hex_str, 16)
        ascii_str += chr(byte_value)
    
    return ascii_str

def decrypto(flag,key):
    sum = 0
    for i in range(32):
        flag[1] -= ((flag[0]  << 4 ^ flag[0] >> 5) + flag[0] ^ key[sum & 3] + sum ^ sum + i) & 0xFFFFFFFF
        sum = (sum - 0x61C88647) & 0xFFFFFFFF
        flag[0] -= ((flag[1] << 4 ^ flag[1] >> 5) +flag[1] ^ key[sum >> 11 & 3] + sum ^ sum + i)& 0xFFFFFFFF

key = [ord(c) for c in "GEEK"]
flag = "f1f186b25a96c782e6c63a0b70b61b5ced6bf84889700d6b09381b5ccb2f24fab1c79e796d822d9cdcc55f760f780e750d65c4afb89084a9e978c3827a8dd81091f28df3a84dbacab4d75f75f19af8e5b90f80fcfc10a5c3d20679fb2bc734c8ccb31c921ac52ad3e7f922b72e24d923fb4ce9f53548a9e571ebc25adf38862e10059186327509463dd4d54c905abc36c26d5312d2cd42c0772d99e50cd4c4665c3178d63a7ffe71ada251c070568d5a5798c2921ec0f7fc3ae9d8418460762930ca6a2dccef51d2a1a8085491b0f82d686ca34774c52d0f0f26449fc28d362c86f3311b8adc4fb1a4497e34e0f0915d"
flag = hex_string_to_32bit_int_array(flag)
sum = 0
temp = [0]*2
for i in range(0,len(flag),2):
    temp[0], temp[1] = flag[i], flag[i+1]
    decrypto(temp,key)
    flag[i], flag[i+1] = temp[0], temp[1]

flag = int_array_to_hex8_array(flag)

print(hex8_array_to_ascii(flag))