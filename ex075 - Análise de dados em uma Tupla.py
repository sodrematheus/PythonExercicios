n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digte o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))
num = (n1, n2, n3, n4)
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'Você digitou o número 3 na {(num.index(3))+1}ª posição')
else:
    print('Você não digitou o número 3.')
print('Você digitou os seguintes números pares: ', end='')
for nn in num:
    if nn % 2 == 0:
        print(nn, end=' ')
