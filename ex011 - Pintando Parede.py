print('Qual a dimensão e a área da minha parede e quantos litros de tinta preciso para pintar-la?')
a = float(input('Digite a altura da sua parede em metros: '))
l = float(input('Digite a largura da sua parede em metros: '))
print('''A dimensão da sua parede é {} x {} e sua área é {:.2f}m².
Sabendo que 1 litro de tinta pinta uma área de 2m², você vai precisar de {:.3f} litros de tinta'''.format(a, l, a*l, (a*l)/2))
