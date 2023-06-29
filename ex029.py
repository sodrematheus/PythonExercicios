v = float(input('Digite sua velocidade em km/h: '))
if v >80:
    print('Multado! Você excedeu o limite permitido que é de 80km/h.')
    print('O valor da sua multa é de R${:.2f}.'.format((v-80)*7))
    print('Dirija com segurança!')
else:
    print('Você está abaixo do limite permitido que é de 80km/h. \nTenha um bom dia! Continue dirigindo com segurança!')
