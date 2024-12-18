t1 = int(input('Digite o primeiro termo da PA: '))
r1 = int(input('Digite a razão da PA: '))
decimo = t1 + (10 - 1) * r1
for c in range(t1, decimo + r1, r1):
    print(c)
