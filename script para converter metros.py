print("<< Olá, vamos converte seu numero de metros pata CENTRIMETROS e MILIMETROS >>")
n = int(input('digite o numero para a conversão: '))
centrimetros = n * 100
milimetros = n * 1000
print('o numero digitado foi: {}M \nque em centrimetros fica: {}CM \n e em milimetros fica: {}MM '.format(n, centrimetros, milimetros))
