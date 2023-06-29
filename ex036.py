casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: '))
tempo = int(input('Quantos anos de financiamento? '))
men = casa / (tempo*12)
print('Para pagar a casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa,tempo, men))
if men < salario*0.3:
    print('Empréstimo aprovado! A prestação está abaixo de 30% do seu salário, como pede a regra.')
else:
    print('Empréstimo rerprovado! A prestação está acima de 30% do seu salário, infligindo a regra.')
