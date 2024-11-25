def reverse_test2(cipher2):
    key = 'SYC'
    length = 18
    result = []
    for i, char in enumerate(cipher2):
        char_code = ord(char) - 1
        char_code ^= ord(key[i % 3])
        result.append(chr(char_code))
    return ''.join(result)

def reverse_test(cipher1, r):
    result = []
    for char in cipher1:
        if 'A' <= char <= 'Z':
            char_code = ((ord(char) - ord('A')) % 26) - r + ord('A')
            result.append(chr(char_code))
        elif 'a' <= char <= 'z':
            char_code = ((ord(char) - ord('a')) % 26) - r + ord('a')
            result.append(chr(char_code))
        elif '0' <= char <= '9':
            char_code = ((ord(char) - ord('0')) % 10) - r + ord('0')
            result.append(chr(char_code))
        else:
            result.append(char)
    return ''.join(result)

def decrypt(input_cipher2, r):
    cipher1 = reverse_test2(input_cipher2)
    original_input = reverse_test(cipher1, r)
    return original_input[:-len(str(r))]