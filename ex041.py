from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
if idade <= 9:
    print('A categoria do(a) atleta de {} anos é Mirim.'.format(idade))
elif idade <= 14:
    print('A categoria do(a) atleta de {} anos é Infantil.'.format(idade))
elif idade <= 19:
    print('A categoria do(a) atleta de {} anos é Junior.'.format(idade))
elif idade <= 25:
    print('A categoria do(a) atleta de {} anos é Senior.'.format(idade))
else:
    print('A categoria do(a) atleta de {} anos é Master.'.format(idade))
