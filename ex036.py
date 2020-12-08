c = float(input('Qual é o valor da casa: R$'))
s = float(input('Qual é o seu salario? '))
a = int(input('Em quantos anos deseja financiar? '))
p = c / (a * 12)
m = s * 30 / 100
print('A prestação da casa sera de R${:.2f}'.format(p))
if p <= m:
    print('Parabens seu finaciamento foi aprovado!! ')
else:
    print('Seu financiamento foi recusado, que pena ;-;!')