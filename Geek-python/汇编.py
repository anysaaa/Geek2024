str = "TTDv^jrZu`Gg6tXfi+pZojpZSjXmbqbmt.&x"
str = [ord(str[i]) for i in range(len(str))]
for i in range(0,36,2):
    str[i]  = str[i] ^ 7
    str[i+1] += 5
for i in range(36):
    print(chr(str[i]),end="")
