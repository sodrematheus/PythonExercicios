a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços? {}'.format(a.isspace()))
print('Só tem números? {}'.format(a.isnumeric()))
print('Só tem letras? {}'.format(a.isalpha()))
print('É alfanumérico? {}'.format(a.isalnum()))
print('Está tudo em maiúsculo? {}'.format(a.isupper()))
print('Está tudo em minúsculo? `{}'.format(a.islower()))
print('Está capitalizada? {}'.format(a.istitle()))
