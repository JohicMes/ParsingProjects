
y =['f','o']
x = ord('a')
z = 0
while z < len(y):
    i = 0
    x = ord('a')
    while i < 26:
        if ord(y[z]) == x:
            print(chr(x))
        x += 1
        i += 1
    z += 1
    