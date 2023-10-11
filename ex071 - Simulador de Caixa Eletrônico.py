print('='*40)
print('{:^40}'.format('BANDO DO SODRÉ'))
print('='*40)
valor = int(input('Qual valor você quer sacar? R$'))
#50
cedula50 = valor // 50
#20
resto50 = valor % 50
cedula20 = resto50 // 20
#10
resto20 = resto50 % 20
cedula10 = resto20 // 10
#1
resto10 = resto20 % 10
cedula1 = resto10 // 1
if cedula50 > 0:
    print(f'Total de {cedula50} cédula(s) de R$50')
if cedula20 > 0:
    print(f'Total de {cedula20} cédula(s) de R$20')
if cedula10 > 0:
    print(f'Total de {cedula10} cédula(s) de R$10')
if cedula1 > 0:
    print(f'Total de {cedula1} cédula(s) de R$1')
