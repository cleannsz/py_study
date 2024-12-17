from random import randint
jogada = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Opções:
0 PEDRA
1 PAPEL
2 TESOURA''')
jokenpo = int(input('Digite sua jogada: '))
print('computador jogou {}'.format(jogada[pc]))
print('jogador jogou {}'.format(jogada[jokenpo]))
if pc == 0:
    if jokenpo == 0:
        print('EMPATE')
    elif jokenpo == 1:
        print('JOGADOR VENCE')
    elif jokenpo == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif pc == 1:
        if jokenpo == 0:
            print('COMPUTADOR VENCE')
        elif jokenpo == 1:
            print('EMPATE')
        elif jokenpo == 2:
            print('JOGADOR VENCE')
        else:
            print('JOGADA INVALIDA')
elif pc == 2:
        if jokenpo == 0:
            print('JOGADOR VENCE')
        elif jokenpo == 1:
            print('COMPUTADOR VENCE')
        elif jokenpo == 2:
            print('EMPATE')
        else:
            print('JOGADA INVALIDA')
