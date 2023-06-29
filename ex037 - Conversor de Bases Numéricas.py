n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Conveter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para hexadecimal''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print('O número {} convertido para binário é igual a {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('O número {} convertido para Octal é igual a {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('O número {} convertido para Hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')
