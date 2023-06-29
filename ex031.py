n = float(input('Qual a distancia(km) da sua viagem: '))
print('Você está prestes a fazer uma viagem de {}km.'.format(n))
if n > 200:
    print('O preço da sua viagem vai ser R${:.2f}'.format(n*0.45))
else:
    print('O preço da sua viagem vai ser R${:.2f}'.format(n*0.50))
