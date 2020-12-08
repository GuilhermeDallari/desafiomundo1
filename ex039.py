from datetime import date
atual = date.today().year
sx = int(input('qual o seu sexo: \n1. masculino\n2. feminino\n:'))
if sx == 1:
    a = int(input('ano de nascimento: '))
    i = atual - a
    al = a + 18
    print('Quem nasceu em {} tem {} anos em {}'.format(a, i, atual))
    if i == 18:
        print('Você tera que se apresentar emediatamente')
    elif i < 18:
        s = 18 - i
        print('faltam {} anos para voce se alistar!'.format(i))
    elif i > 18:
        s = i - 18
        print('Você ja deveria ter se alistado á {} anos'.format(s))

else :
    print('Voce não precisa se alistar!')

