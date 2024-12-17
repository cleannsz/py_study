num = int(input('Digite um numero inteiro: '))
base = int(input('Escolha a base de conversão, Digite 1 para binário, 2 para octal e 3 para hexadecimal: '))
if base == 1:
    binario = bin(num)
    print('O número digitado em binário é igual a: {}'.format(binario[2:]))
elif base == 2:
    octal = oct(num)
    print('O número digitado em octal é igual a: {}'.format(octal[2:]))
elif base == 3:
    hexadecimal = hex(num)
    print('O número digitado em hexadecimal é igual a: {}'.format(hexadecimal[2:]))
