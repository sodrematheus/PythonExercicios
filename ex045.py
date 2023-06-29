import time
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jog = int(input('Escolha sua jogada: '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('=' * 25)
print('O computador jogou: {}'.format(itens[cpu]))
print('Você jogou: {}'.format(itens[jog]))
print('=' * 25)
if jog == cpu:
	print('Empate!')
elif jog == 0 and cpu == 1:
	print('Você perdeu!')
elif jog == 0 and cpu == 2:
	print('Você ganhou!')
elif jog == 1 and cpu == 0:
	print('Você ganhou!')
elif jog == 1 and cpu == 2:
	print('Você perdeu!')
elif jog == 2 and cpu == 0:
	prinr('Você perdeu!')
elif jog == 2 and cpu == 1:
	print('Você ganhou!')
