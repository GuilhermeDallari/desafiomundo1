import random
n1 = input('primeiro aluno : ')
n2 = input('sugundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('quarto aluno: ')
e = [n1, n2, n3, n4]
r = random.choice(e)
print('O escolhido foi {}'.format(r))