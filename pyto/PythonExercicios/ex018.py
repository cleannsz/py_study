import math
angulo = float(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o seno: {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a tangente {:.2f}'.format(angulo, tangente))