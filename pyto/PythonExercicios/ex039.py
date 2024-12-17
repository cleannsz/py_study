idade = int(input('Digite sua idade: '))
if idade < 18:
    print('Você ainda vai se alistar ao serviço militar')
elif idade == 18:
    print('Está na hora de se alistar')
elif idade > 18:
    print('Ja passou do tempo de se alistar')
