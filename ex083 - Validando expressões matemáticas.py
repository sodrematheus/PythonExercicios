expressao = input('Digite a expressão: ')
abre = expressao.count('(')
fecha = expressao.count(')')
if abre - fecha == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressção esta incorreta!')
