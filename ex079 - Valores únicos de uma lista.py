valores = []
while True:
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar in 'N':
        break
print('=-'*40)
valores.sort()
print(f'Você digitou os valores {valores}')
