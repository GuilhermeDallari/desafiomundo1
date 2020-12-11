from datetime import date
ano = date.today().year
n = int(input('Ano de nascimento do atleta: '))
i = ano - n
print('O atleta  tem {} Anos'.format(i))
if i <= 9:
    print('O atleta é classificado como MIRIM')
elif i > 9 and i < 14:
    print('O atleta é classificado como INFANTIL')
elif i > 14 and i < 19:
    print('O atleta é classificado como JUNIOR')
elif i > 19 and i < 25:
    print('O atleta é classificado como SENIOR')
else:
    print('O atleta é um MASTER')
