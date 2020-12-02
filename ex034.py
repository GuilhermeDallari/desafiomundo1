n1 = float(input('Qual é seu salario atual? '))
if n1 <= 5000:
    salario = n1 + (n1 * 15 / 100)
    print('Seu novo salario sera de R${:.2f}.'.format(salario))
else:
    salario = n1 + (n1 * 10 /100)
    print('Seu novo salario é de R${:.2f}.'.format(salario))