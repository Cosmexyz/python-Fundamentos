import math
numero = float(input('Digite o angulo desejado: '))
angulo = math.radians(numero)
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print('O SENO de {} é igual a: {:.2f}'.format(numero, seno))
print('O COSSENO de {} é igual a {:.2f}'.format(numero, cosseno))
print('A TANGENTE de {} é igual a {:.2f}'.format(numero, tangente))
