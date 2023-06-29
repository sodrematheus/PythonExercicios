from datetime import date
genero = input('Seu gênero é Masculino ou Feminino? ').strip().upper()
if genero == 'FEMININO':
    print('Fique tranquila, pessoas do gênero feminino não precisa se alistar.')
else:
    ano = int(input('Digite seu ano de nascimento: '))
    idade = date.today().year - ano
    print('Quem nasceu em {} completa {} anos em {}.'.format(ano, idade, date.today().year))
    if idade > 18 and genero == 'MASCULINO':
        print('Você já deveria ter se alistado há {} ano(s), em {}.'.format(idade - 18, ano + 18))
    elif idade < 18 and genero == 'MASCULINO':
        print('Ainda falta(m) {} ano(s) para o alistamento, em {}.'.format(18 - idade, ano + 18))
    elif idade == 18 and genero == 'MASCULINO':
        print('Você tem que se alistar esse ano.')
#EU APRIMOREI O QUE ELE PEDE NO EXERCICIO PERGUNTANDO O SEXO DO USUÁRIO
