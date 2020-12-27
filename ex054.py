from datetime import date
a = date.today().year
m = 0
ma = 0
for p in range (1, 8):
    n = int(input('Em que ano a {}ª pessoa nasceu? '.format(p)))
    i = a - n
    if i >= 21:
        ma += 1
    else:
        m += 1
print('{} pessoas sao de maior'.format(ma))
print('{} pessoas sao de menor'.format(m))