import random
import time
print('-=-'*19)
print(' Eu vou pensar em um número entre 0 e 5, tente advinhar!')
print('-=-'*19)
n = int(input('Digite o número: '))
m = random.randint(0, 5)
print('-=-'*6)
print('Processando... 🤔')
print('-=-'*6)
time.sleep(1)
if n == m:
    print('Você acertou!!! 😀')
    print('-=-' * 6)
else:
    print('Você errou... 😢')
    print('-=-' * 6)
