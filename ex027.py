n1 = str(input('digite seu nome completo: ')).strip()
n2 = n1.split()
print('Seu primeiro nome é {}'.format(n2[0]))
print('seu ultimo nome é {}'.format(n2[len(n2)-1]))
