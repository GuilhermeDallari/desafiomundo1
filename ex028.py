from random import randint
from time import sleep
c = randint(0,5)#randon
print('=-='*10)
print('Vou pensar em um numero tente advinhar...')
print('=-='*10)
j = int(input('Em que numero eu pensei? '))
print('LENDO SUA MENTE...')
sleep(3)
if j == c:
    print('PARABENS VOCE GANHOU DA MAQUINA, AINDA TEMOS CHANCES KK!! ')
else:
    print('GAME OVER! EU PESEI NO NUMERO {} E NAO NO {}!'.format(c, j))