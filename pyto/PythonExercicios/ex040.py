nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('REPROVADO')
elif 5 <= media < 7:
    print('RECUPERACAO')
elif media >= 7:
    print('APROVADO')
