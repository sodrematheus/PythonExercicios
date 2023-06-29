from random import randint
pc = randint(0, 10)
print('''Pensarei um número de 0 a 10.
Tente Advinhar!
''')
acertou = False
palpites = 0
while not acertou:
	jogador = int(input('Qual é o seu palpite? '))
	palpites += 1
	if pc == jogador:
		acertou = True
	elif jogador > 10 or jogador < 0:
		print('Valor inválido. Digite um número de 0 a 10')
	else:
		if jogador > pc:
			print('Menos... Tente novamente!')
		if jogador < pc:
			print('Mais... Tente novamente!')
print('Com {} tentativas. Você acertou!!!'.format(palpites))

