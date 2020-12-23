from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
c = randint(0, 2)
print(''' ESCOLHA SUA ARMA 
0. PEDRA
1. PAPEL
2. TESOURA''')
e = int(input('Qual arma você escolheu ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('*=' * 10)
print('O mestre escolheu {}'.format(itens[c]))
print('voce escolheu {}'.format(itens[e]))
print('*=' * 10)
if c == 0: #pedra
    if e == 0:
        print('Empate')
    elif e == 1:
        print('Voce venceu!!')
    elif e == 2:
        print('O mestre ganhou!')
    else:
        print('jogada invalida!')
elif c == 1: #papel
    if e == 0:
        print('O mestre ganhou! ')
    elif e == 1:
        print('empate')
    elif e == 2:
        print('Voce venceu! ')
    else:
        print('jogada invalida!')

elif c == 2: #tesoura
    if e == 0:
        print('Voce venceu! ')
    elif e == 1:
        print('O mestre venceu! ')
    elif e == 2:
        print('empate')
    else:
        print('jogada invalida!')