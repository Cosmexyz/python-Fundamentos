tentativas = 3

while tentativas:
    login = input('DIgite a senha para logar: ') 

    if login == 'python123':
        print('Acesso liberado!!')
        break

    else:
       tentativas = tentativas - 1
       print('Senha incorreta. Tentativas restantes {}'.format(tentativas))
    
    if tentativas == 0:
        print('cartão bçoqueado, vá a agencia para desbloquear')
        