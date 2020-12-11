n = float(input('primeira nota: '))
sn = float(input('segunda nota: '))
m = (n + sn) / 2
print('tendo em vista que a media do aluno foi {:.1f}'.format(m))
if m >= 5 and m < 7:
    print('O aluno esta de recuperação')
elif m < 5:
    print('O aluno esta reprovado')
elif m >= 7:
    print('O aluno esta aprovado')

