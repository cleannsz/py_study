print('Calculadora de preços por viagem, R$0,50 por km ate 200km e R$0,45 para viagens acima de 200km')
num1 = float(input('Quantos km vc vai percorrer na sua viagem? '))
if num1 <= 200:
    num1 = num1 * 0.50
    print('Sua viagem custará R${:.2f}'.format(num1))
else:
    num1 = num1 * 0.45
    print('Sua viagem custará R${:.2f}'.format(num1))
