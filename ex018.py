from math import radians, sin, cos, tan
an = float(input('Digite o ângulo: '))
seno = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('O seno do ângulo {} é {:.2f}'.format(an, seno))
print('O cosseno do ângulo {} é {:.2f}'.format(an, cos))
print('A tangente do ângulo {} é {:.2f}'.format(an, tan))
