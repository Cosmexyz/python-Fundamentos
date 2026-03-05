print("<< Olá, vamos converte seu numero de metros pata CENTIMETROS e MILIMETROS >>")
n = float(input('digite o numero para a conversão: '))
cm = n * 100
mm = n * 1000
dm = n * 10
km = n / 1000
dam = n / 10
hm = n / 100
print('o numero digitado foi: {}m \nque em centimetros fica: {:.0f}cm \ne em milimetros fica: {:.0f}mm \nE em decimetros fica: {}dm'.format(n, cm, mm, dm))
print('Em kilometros fica: {}km \nE em decametros fica: {}dam \nEn hectometros fica: {}hm'.format(km, dam, hm))

