from time import sleep
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

opcao = 0
while opcao != 5:
	print('-==' * 18)
	print('''Qual das operações abaixo você gostaria de ultilizar?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Qual é o maior?
[ 4 ] Digitar novos números
[ 5 ] Encerrar programa''')
	opcao = int(input('Qual é sua opção? '))
	if opcao == 1:
		print('O resultado de {} + {} é {}'.format(a, b, a + b))
	elif opcao == 2:
		print('O resultado de {} x {} é {}'.format(a, b, a * b))
	elif opcao == 3:
		if a > b:
			print('Entre {} e {} o maior é {}'.format(a, b,  a))
		if b > a:
			print('Entre {} e {} o maior é {}'.format(a, b, b))
		if a == b:
			print('Os dois valores são iguais.')
	elif opcao == 4:
		print('\nInforme os números novamente!')
		a = int(input('Digite o primeiro número: '))
		b = int(input('Digite o segundo número: '))
	elif opcao == 5:
		print('\nFinalizando...')
	else:
		print('Opção inválida. Escolha uma das opções acima.')
		print('-==' * 15)
	sleep(2)
print('Programa encerrado. Volte sempre!')
