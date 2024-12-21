sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]

while sexo != 'M' and sexo != 'F':
    print('Incorreto. Por favor, digite novamente.')
    sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
print('Vc eh {}'.format(sexo))
