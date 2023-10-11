n = cont = 0
while True:
    print('-'*34)
    n = int(input('Quer ver a tabuada de qual número? '))
    print('-' * 34)
    if n < 0:
        break
    for cont in range(1,11):
        print(f'{n} x {cont} = {n*cont}')
print('Programa tabuada encerrado. Volte sempre!')
