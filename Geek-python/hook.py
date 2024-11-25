str = "zoXpih^lhX6soX7lr~DTHtGpX|"
str = [ord(str[i]) for i in range(len(str))]

key = [7,7,0x0A,7,18,62,77,7,7,7,7,0,20,17,33,51,43,3,47,7,7,7,89,48,83,9,0]

for i in range(len(str)):
    str[i] ^= key[i]


for i in str:
    print(chr(i),end="")