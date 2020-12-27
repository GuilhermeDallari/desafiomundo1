l = 0
g = 0
for p in range(1, 6):
    pe = float(input('peso da {}ª pessoa: '.format(p)))
    if p == 1:
        l = p
        g = p
    else:
        if pe > g:
            g = pe
        if pe < l:
            l = pe
print('O maior peso foi {}Kg '.format(g))
print('O menor peso foi {}Kg '.format(l))