print('VAMOS VERIFICAR SE A FRASE É UM PALÍNDROMO!\n')
frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
#[::-1} onde o primeiro : significa que eu quero começar no inicio da string e o segundo : significa que eu quero ir até o final da string
#Ou seja, colocando os dois : significa que eu quero usar toda string, e o -1 significa que eu quero inverter a string.
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
