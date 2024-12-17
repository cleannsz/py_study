print('Digite tres valores para saber se eles podem formar um triangulo')
r1 = float(input('Reta 1 = '))
r2 = float(input('Reta 2 = '))
r3 = float(input('Reta 3 = '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Eles podem formar um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Eles nao podem formar um triangulo')
