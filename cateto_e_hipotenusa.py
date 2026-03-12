from math import hypot
cateto_oposto = float(input('Digite o número do cateto oposto: '))
cateto_adjacente = float(input('Digite o número do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print('a hipotenusa vai ser: {:.2f}'.format(hipotenusa))
