maior = 0
menor = 0
for p in range(0, 5):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p+1)))
    if p == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))
