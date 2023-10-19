lista = []
listapar = []
listaimpar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar?[S/N] ').strip().upper()[0]
    if continuar in 'N':
        break
for n in lista:
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de impares é {listaimpar}')
