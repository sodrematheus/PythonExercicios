print('-'*30)
print('{:^30}'.format('LOJA DO SODRÉ'))
print('-'*30)
total = produtos1000 = menor = cont = 0
barato = ' '
while True:
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        produtos1000 += 1
    if cont == 1 or preco < menor:
        barato = produto
        menor = preco
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar [S/N]? ').strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {produtos1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi o {barato} que custou R${menor:.2f}')
