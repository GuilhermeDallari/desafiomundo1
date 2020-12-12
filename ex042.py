l = float(input('primeiro segmento: '))
l2 = float(input('segundo segmento: '))
l3 = float(input('terceiro segmento: '))
if l < l2 + l3 and l2 < l + l3 and l2 < l3 + l:
    print('É possivel formar um triangulo', end=' ')
    if l == l2 == l3:
        print('EQUILATERO')
    elif l != l2 and l != l3 and l2 != l3:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('NAO é possivel formar um triangulo')
