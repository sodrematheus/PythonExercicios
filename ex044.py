print('{:=^40}'.format(' Mercado Sodré '))
p = float(input('Valor total da compra: R$'))
print('''Formas de pagamento
[ 1 ] Dinheiro (10% de desconto)
[ 2 ] PIX (10% de desconto)
[ 3 ] Débito (5% de desconto)
[ 4 ] Crédito (À vista 5% de desconto,
2x sem juros, 3x ou mais 20% de juros''')
f = int(input('Digite a opção para forma de pagamento: '))
if f == 1:
    print('''Forma de pagamento: Dinheiro
    Total a pagar: R${:.2f}'''.format(p * 0.9))
elif f == 2:
    print('''Forma de pagamento: PIX
    Total a pagar: R${:.2f}
    Leia o QR CODE abaixo:'''.format(p * 0.9))
elif f == 3:
    print('''Forma de pagamento: Débito
    Total a pagar: R${:.2f}
    Aproxime ou insire o cartão'''.format(p * 0.95))
elif f == 4:
    print('''Forma de pamento: Crédito
[ 1 ] 1x
[ 2 ] 2x
[ 3 ] 3x
[ 4 ] 4x
[ 5 ] 5x''')
    parcelas = int(input('Quantas parcelas? '))
    if parcelas == 1:
        print('1x Total: R${:.2f}'.format(p * 0.95))
    elif parcelas == 2:
        print('''2x de R${:.2}'
Total: R${:.2f}'''.format((p * 1.2)/parcelas, p))
    elif parcelas >= 3:
        print('''{}x de R${:.2f}
Total: R${:.2f}
Aproxime ou Insira o seu cartão'''.format(parcelas, (p * 1.2)/parcelas, p * 1.20))
else:
    print('Opção inválida. Tente novamente.')
