import random
n = input('Gostaria de fazer o sorteio (S/N)? ').upper()
while n == 'S':
    a1 = input('Digite o nome do primeiro aluno: ')
    a2 = input('Digite o nome do segundo aluno: ')
    a3 = input('Digite o nome do terceiro aluno: ')
    a4 = input('Digite o nome do quarto aluno: ')
    lista = [a1, a2, a3, a4]
    print('O aluno escolhido foi: {}'.format(random.choice(lista)))
    n = input('Gostaria de fazer um novo sorteio? (S/N) ').upper()
print('Volte sempre!')
