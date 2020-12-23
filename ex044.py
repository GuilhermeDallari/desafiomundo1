print('{:=^40}'.format(' LOJAO DO PYTHON '))
n = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO 
1. Á vista dinheiro/cheque
2. Á vista cartão 
3. 2x no cartão 
4. 3x ou mais no cartão''')
m = int(input('Qual é a modo de pagamento? '))
if m ==1:
    total = n - (n * 10 / 100)
elif m == 2:
    total = n - (n * 5 / 100)
elif m == 3:
    total = n
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R${:.2f}'.format(parcela))
elif m == 4:
    total = n + (n * 20 / 100)
    p1 = int(input('quantas parcelas? '))
    parcela = total / p1
    print('Sua compra sera parcelada em {}x de R${:.2f}'.format(p1, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(n, total))