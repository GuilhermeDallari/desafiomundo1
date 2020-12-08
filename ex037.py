num = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão:\n1. converter para BINÁRIO\n2. converter para OCTAL\n3. converter para HEXADECIMAL')
o = int(input('sua escolha: '))
if o == 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(num)[2:]))
elif o == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif o == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida')