print('Calculando PA (Progressão aritmética) dos 10 primeiros termos\n')
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
n = p + (10 - 1) * r
for c in range(p, n + r, r):
    print(c, end=' -> ')
print('Fim.')
