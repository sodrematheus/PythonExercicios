a = float(input('Digite o primeiro segmento de reta: '))
b = float(input('Digite o segundo segmento de reta: '))
c = float(input('Digite o terceiro segmento de reta: '))
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('Os segmentos acima podem formar um Triângulo Equilátero')
    elif a == b or a == c or b == c:
        print('Os segmentos de reta acima podem formar um triângulo Isósceles.')
    elif a != b != c:
        print('Os segmentos de reta acima podem formar um triângulo Escaleno.')
else:
    print('Os segmentos de reta acima não podem formar um triângulo.')
