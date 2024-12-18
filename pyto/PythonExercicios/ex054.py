n1 = 2024
n2 = 0
n3 = 21
idade = 0
for c in range(0, 6):
    ano = int(input('Digite o ano de nascimento: '))
    n2 = n1 - ano
    if n2 >= 21:
        idade +=1
print('{} Pessoas atingiram a maioridade'.format(idade))