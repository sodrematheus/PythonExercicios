continuar = 'S'
soma = 0
cont = 0
media = 0
maior = 0
menor = 0
while continuar == 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = input('Quer continuar?[S/N] ').upper().strip()
media = soma / cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
