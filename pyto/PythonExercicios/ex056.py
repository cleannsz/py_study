year = 0
age = 0
velho = 0
mid = 0

for c in range(0, 4 ):

    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))

    mid = mid + idade

    sexo = input('Digite seu sexo (M/F): ')
    if sexo == 'M':
        if idade > year:
            year = idade
            velho = nome

    if sexo == 'F':
        if idade < 20:
            age = age + 1

mid = mid / 4

print('A media de idade do grupo é {}'.format(mid))
print('O nome do homem mais velho é {}'.format(velho))
print('{} Mulher(s) tem menos que 20 anos'.format(age))