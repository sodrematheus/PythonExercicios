a = float(input('Digite sua primeira nota: '))
b = float(input('Digite sua segunda nota: '))
m = (a + b) / 2
if m >= 7.0:
    print('Sua média foi {:.1f}. Parabéns! Você está aprovado(a)'.format(m))
elif m < 5.0:
    print('Sua média foi {:.1f}. Você está reprovado. Estude mais!'.format(m))
else:
    print('Sua média foi {:.1f}. Você está de recuperação. Estude mais!'.format(m))
