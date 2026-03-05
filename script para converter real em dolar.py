print('<<< Ola, converta aqui seu R$ para US$ >>>')
real = float(input('quantos R$ vc tem? '))
dolar = real / 3.27
print('Após a conversão do R${:.0f}, você terá exatos US${:.2f} '.format(real, dolar))

