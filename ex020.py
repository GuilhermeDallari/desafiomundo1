import random
n1 = input('primeiro nome: ')
n2 = input('segundo nome: ')
n3 = input('terceiro nome: ')
n4 = input('quarto nome: ')
l = [n1, n2, n3, n4]
r = random.shuffle(l)
print('a ordem de apresenração é {}'.format(l))