p1 = int(input('Digite um numero para saber se ele é ou nao eh primo: '))
tot = 0
for c in range(1, p1 + 1):
    if p1 % c == 0:
        tot += 1
if tot == 2:
    print('Esse numero eh primo')
else:
    print('Esse numero nao eh primo')