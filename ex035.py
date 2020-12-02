print('=*=' * 20)
print('analizador de Triangulos')
print('=*=' * 20)
r1 = float(input('primeiro seguimento: '))
r2 = float(input('segundo seguimento: '))
r3 = float(input('terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos podem formar um triângulo')
else:
    print('Os segmentos acima NÃO podem formar um triangulo')
