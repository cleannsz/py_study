n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

opcao = int(input('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair
------> '''))

while opcao != 5:

    if opcao == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))

    if opcao == 2:
        print('{} * {} = {}'.format(n1, n2, n1 * n2))

    if opcao == 3:
        if n1 > n2:
            print('{} > {}'.format(n1, n2))
        else:
            print('{} < {}'.format(n1, n2))

    if opcao == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))

    opcao = int(input('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair
    ------> '''))
