v = int(input('Qual a velocidade atual do veiculo? '))
if v > 80:
    print('Voce acaba de ser MULTADO!! Voce excedeu o limite de 80km/h\nVoce foi multado em : R${} '.format((v - 80) * 7))
print('Tenha um bom dia, dirija com segurança!!')