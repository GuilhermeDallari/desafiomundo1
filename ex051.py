p = int(input('primeiro termo: '))
r = int(input('Razao: '))
d = p + (10 - 1) * r
for x in range (p, d, r):
    print('{} '.format(x), end='> ')