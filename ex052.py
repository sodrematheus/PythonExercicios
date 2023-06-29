n = int(input('Digite o número para saber se é um número primo: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\33[33m', end=' ')
        cont += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n O número {} é divisivel por {} números.'.format(n, cont))
if cont == 2:
    print('O {} é um número primo.'.format(n))
else:
    print('O {} não é um número primo'.format(n))
