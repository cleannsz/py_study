print('Caso queira encerrar digite 999')
n1 = int(input('Digite um valor inteiro: '))

n2 = 0
cont = 0

while n1 != 999:
    cont += 1
    n2 += n1
    print('Caso queira encerrar digite 999')
    n1 = int(input('Digite um valor inteiro: '))
    
print('Foram digitados {} numeros e a soma deles é igual a {}'.format(cont, n2))