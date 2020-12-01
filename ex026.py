n1 = str(input('digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(n1.count('A')))
print('A primeira letra A apareceu na posição {}'.format(n1.find('A')+1))
print('A ultima letra A aprece na posição {}'.format(n1.rfind('A')+1))