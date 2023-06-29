s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite o {}º valor inteiro: '.format(c+1)))
    if n % 2 == 0:
        s += n
        cont += 1
print('Você digitou {} números pares e a soma deles é {}'.format(cont, s))
