valor = float(input('Digite o valor do produto: '))
print('Digite abaixo usando de 1 a 4 a forma de pagamento: ')
print('1 - à vista dinheiro/ chaque: 10% de desconto')
print('2 - à vista no cartão: 5% de desconto')
print('3 - em até 2x no cartão: preço normal')
print('4 - 3x ou mais no cartão: 20% de juros')
pagamento = int(input('Qual será a forma de pagamento? '))
if pagamento == 1:
    valor = valor * 0.90
    print('O valor do protudo será de R${:.2f}'.format(valor))
elif pagamento == 2:
    valor = valor * 0.95
    print('O valor do produto será de R${:.2f}'.format(valor))
elif pagamento == 3:
    print('O valor será de R${:.2f}'.format(valor))
elif pagamento == 4:
    valor = valor * 1.20
    print('O valor do produto será de R${:.2f}'.format(valor))
