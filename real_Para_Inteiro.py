'''n = float(input('Digite um número: '))
print('O número digitado é {}, que está em sua real. \nEm sua forma inteira fica: {:.0f}.'.format(n, n))'''

#ou pode ser feito da seguinte maneira#

from math import trunc
n = float(input('Digite um número: '))
print('O valor digitado foi: {}, que está em sua forma real. \nEm sua forma inteira fica: {}.'.format(n, trunc(n)))

