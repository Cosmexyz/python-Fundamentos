
semaforo = 'VERMELHO'

while True:
    
    açao = input('O semaforo está {} você vai: AVANÇAR, FREAR ou PARAR:\n'.format(semaforo))

    if semaforo == 'VERMELHO' and açao == 'parar':
       semaforo = 'VERDE'
       print(semaforo)

    elif semaforo == 'VERDE' and açao == 'avançar':
         semaforo = 'AMARELO'
         print(semaforo)

    elif semaforo == 'AMARELO' and açao == 'frear':
         semaforo = 'VERMELHO'
         print(semaforo)

    else:
        print('Comando invalido')
      
    