from random import randint
print('=-'*20)
print('       VAMOS JOGAR PAR OU IMPAR')
cont = 0
while True:
    print('=-' * 20)
    pi = input('Par ou ímpar? [P/I] ').upper().strip()[0]
    cpu = randint(0, 10)
    j = int(input('Digite um valor de 0 a 10: '))
    soma = j + cpu
    if pi not in 'PpIi' or j < 0 or j > 10:
        print('Uma das alternativas inválida, digite P ou I para par ou Ímpar e digite um valor entre 0 e 10.')
        cont -= 1
    elif pi == 'P':
        if soma % 2 == 0:
            print('-' * 40)
            print(f'Você jogou {j} e o computador jogou {cpu}. Total de {soma} deu Par.')
            print('-' * 40)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
        else:
            print('-' * 40)
            print(f'Você jogou {j} e o computador jogou {cpu}. Total de {soma} deu Impar.')
            print('-' * 40)
            print('Você PERDEU!')
            break
    elif pi == 'I':
        if soma % 2 != 0:
            print('-' * 40)
            print(f'Você jogou {j} e o computador jogou {cpu}. Total de {soma} deu Impar.')
            print('-' * 40)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
        else:
            print('-' * 40)
            print(f'Você jogou {j} e o computador jogou {cpu}. Total de {soma} deu Par.')
            print('-' * 40)
            print('Você PERDEU!')
            break
    cont += 1
print(f'GAME OVER! Você venceu {cont} vez(es).')
