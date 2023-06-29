a = float(input('Digite o primeiro númeiro: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
#Verificando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando o maior número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi o {}'.format(menor))
print('O maior valor digitado foi o {}'.format(maior))
