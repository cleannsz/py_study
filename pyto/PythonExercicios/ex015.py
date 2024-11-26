alugados = float(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? '))
n1 = alugados * 60
n2 = km * 0.15
n3 = n1 + n2
print('O valor total é R${}0'.format(n3))
