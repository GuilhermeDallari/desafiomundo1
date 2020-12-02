n = float(input('Qual a distancia de sua viagem em Km: '))
p = n * 0.50 if n <= 150 else n * 0.45
print('O valor de sua viagem sera de R${:.2f}.'.format(p))