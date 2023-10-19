from random import randint
from time import sleep
jogos = []
print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)
quantj = int(input('Quantos jogos você quer que eu sorteie? '))
print()
print(f'SORTEANDO {quantj} jogos!')
for c in range(0, quantj):
    print(f'JOGO {c+1}: ', end='')
    lista = []
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    print(lista)
    sleep(1)
    lista.clear()
print()
print('BOA SORTE!!!')
