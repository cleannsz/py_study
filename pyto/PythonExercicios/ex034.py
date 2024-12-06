salario = float(input('Digite seu salario para calcularmos o aumento: '))
if salario > 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10
print('voce teve um aumento de {}'.format(aumento))
