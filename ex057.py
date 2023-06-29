s = input('Digite seu sexo [M/F]: ').strip().upper()[0]
while s != 'M' and s != 'F':
    print('Respota inválida!')
    s = input('Digite seu sexo [M/F]: ').strip().upper()[0]
if s == 'M':
    print('Seu sexo é masculino, obrigado pela resposta.')
if s == 'F':
    print('Seu sexo é feminino, obrigado pela resposta.')
