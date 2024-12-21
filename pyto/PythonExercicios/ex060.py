n1 = int(input('Digite um valor para saber seu fatorial: '))
n2 = n1 - 1
while n2 > 1:
    n1 *= n2
    n2 -= 1
print('O fatorial eh {}'.format(n1))