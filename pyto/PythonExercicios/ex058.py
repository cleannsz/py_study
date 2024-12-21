num1 = 2
num2 = int(input('Digite um numero de 1 a 5 e direi se acertou: '))
num3 = 0
while num1 != num2:
    print('Errou tente novamente: ')
    num3 += 1
    num2 = int(input('Digite um numero de 1 a 5 e direi se acertou: '))
print('Voce acertou depois de {} tentativas'.format(num3))