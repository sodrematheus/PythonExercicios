homemvelho = ''
homemvelhoidade = 0
mulhermenor = 0
somaidade = 0
mediaidade = 0
for n in range(0,4):
    print('---{}ª Pessoa---'.format(n+1))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip().upper()
    somaidade += idade
    if sexo == 'M':
        homemvelho = nome
        homemvelhoidade = idade
    else:
        if sexo == 'M' and idade > homemvelhoidade:
            homemvelhoidade = idade
            homemvelho = nome
    if sexo == 'F' and idade < 20:
        mulhermenor += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {:.2f} anos'.format(mediaidade))
if 'M' in sexo:
    print('O homem mais velho se chama {} e ele tem {} anos.'.format(homemvelho.capitalize(), homemvelhoidade))
else:
    print('Não tem nenhum homem entre os relacionados.')
if 'F' in sexo and idade < 20:
    print('Ao todo são {} mulheres menores de 20 anos.'.format(mulhermenor))
else:
    print('Não tem mulher com idade menor a 20 anos nos relacionados.')
