p = float(input('Digite seu peso(kg): '))
a = float(input('Digite sua altura(m): '))
imc =  p / (a ** 2)
print('Seu IMC é {:.1f}.'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso ideal.')
elif imc <= 25:
    print('Você está dentro do peso ideal.')
elif imc <= 30:
    print('Você está em sobrepeso.')
elif imc <= 40:
    print('Você está em obesidade.')
else:
    print('Você está em obesidade mórbida.')
