print('<<< Ola, vamos calcular quanta tinta sera necessaria para pintar a sua parede >>> ')
altura = float(input('digite a altura da parede: '))
largura = float(input('digite a largura da parede: '))
area = altura * largura
Ltinta = area / 2
print('a área da sua parede é: {:.0f}m2'.format(area))
print('sabendo que a area é: {:.0f}m2 a quantidades de litros de tinta é: {}m2'.format(area, Ltinta))
