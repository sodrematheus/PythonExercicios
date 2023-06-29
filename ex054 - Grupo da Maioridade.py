from datetime import date
maior = 0
menor = 0
for c in range(0, 7):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c+1)))
    hoje = date.today().year
    if hoje - ano >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade\nE {} pessoas menores de idade'.format(maior, menor))
