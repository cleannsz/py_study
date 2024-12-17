ano = int(input('Digite seu ano para saber sua categoria: '))
idade = (ano - 2024)
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SENIOR')
elif idade >= 21:
    print('MASTER')
