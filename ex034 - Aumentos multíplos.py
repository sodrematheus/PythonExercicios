s = float(input('QUal é o salário do funcionário? R$'))
if s <= 1250:
    print('Seu novo salário é R${}, com o aumento de 15%'.format(s*1.15))
else:
    print('Seu novo salário é R${}, com o aumento de 10%'.format(s*1.10))
