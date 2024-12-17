casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} a prestação será de R${:.2f}'.format(casa, prestacao))
if prestacao <= minimo:
    print('EMPRESTIMO CONCEDIDO')
else:
    print('EMPRESTIMO NEGADO')
