
print('<<< Ola, vamos calcular o valor do aluguel do seu carro alugado >>>')
print('-' * 15)
diasCarro = int(input('qunatos dias você ficou com o carro? '))
kmCarro = int(input('qunatos Km você fez no carro? '))
diariaCarro = 60
diariakm = 0.15
valorCarro = diasCarro * diariaCarro
valorKm = kmCarro * diariakm
valorFinal = valorCarro + valorKm
print('Você ira pagar o total de: R${}'.format(valorFinal))

