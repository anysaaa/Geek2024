key = "GEEK"
str = "0A161230300C2D0A2B303D2428233005242C2D26182206233E097F133A"
flag = [int(str[i:i+2],16) for i in range(0,len(str),2)]
for i in range(len(flag)):
    flag[i] ^= ord(key[i%4])
    print(chr(flag[i]),end="")
