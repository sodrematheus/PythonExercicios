pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] >= maior:
            maior = dados[1]
        if dados[1] <= menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar?[S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior:.1f}kg. Peso de',end=' ')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nO menor peso foi {menor:.1f}kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')
