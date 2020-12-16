a = float(input('qual é a sua altura? '))
p = float(input('qual é o seu peso? '))
imc = p / (a * a)
print('O seu imc é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Voce esta abaixo do peso ideal!')
elif imc > 18.5 and imc <= 25:
    print('Voce esta no peso ideal !')
elif imc > 25 and imc <= 30:
    print('Voce esta com sobrepeso !')
elif imc > 30 and imc <= 40:
    print('Voce esta com obesidade! ')
elif imc > 40:
    print('Voce esta com obesidade mórbida !')