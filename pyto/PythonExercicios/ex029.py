vel = float(input('Digite a velocidade em Km/h: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Voce foi multado, essa multa custara R$7,00 por cada km acima da velocidade.')
    print('Sua multa foi de R${:.2f}'.format(multa))
else:
    print('Voce esta dentro do limite de velocidade, boa viagem!')
