from math import hypot
co = float(input('Digite o comprimento(m) do cateto oposto do triângulo retângulo: '))
ca = float(input('Digite o comprimento(m) do cateto adjacente do triângulo retângulo: '))
print('A hipotenusa desse triângulo retângulo é {}'.format(hypot(co, ca)))
