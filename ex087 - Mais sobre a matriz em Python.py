matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = soma3c = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite  um para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        if c == 2:
            soma3c += matriz[l][c]
for c in matriz[1]:
    if c > maior:
        maior = c
print('-='*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-='*20)
print(f'A soma dos valores pares é {somap}.')
print(f'A soma dos valores da terceira coluna é {soma3c}.')
print(f'O maior valor da segunda linha é {maior}.')
