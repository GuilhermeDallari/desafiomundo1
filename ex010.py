n1 = float(input('converta agora uma quantia em R$: '))
dolar = n1 / 5.33
euro = n1 / 6.33
print('com R${:.2f} voce terá U$ {:.2f}'.format(n1, dolar))
print('com R$ {:.2f} voce terá EU$ {:.2f}'.format(n1, euro))