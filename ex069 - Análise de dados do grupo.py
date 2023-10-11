cont18 = conth = contm20 = 0
sexo = ' '
continuar = ' '
while True:
    print('-'*30)
    print('     CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    while sexo not in 'MmFf':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        conth += 1
    if idade < 20 and sexo == 'F':
        contm20 += 1
    print('-'*30)
    while continuar not in 'SN':
        continuar = input('Quer continuar [S/N]? ').strip().upper()[0]
    print('-'*30)
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont18}')
print(f'Total de homens cadastrados: {conth}')
print(f'Total de mulheres com menos de 20 anos: {contm20}')
