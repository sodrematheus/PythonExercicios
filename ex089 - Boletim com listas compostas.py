alunos = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], [media]])
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar?[S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
cont = 0
print('-='*20)
print('Nª  NOME           MÉDIA')
print('-'*24)
for i, c in alunos:
    print(f'{i+1:<4}{c[0]:<15}{c[2]}')
print('-='*20)
mostrar = 0
while mostrar != 999:
    mostrar = int(input('Mostrar notas de quais alunos?(999 interrompe) '))
    print(f'Notas de {alunos[mostrar-1][0]} são {alunos[mostrar-1][1]}')
print('VOLTE SEMPRE!')
