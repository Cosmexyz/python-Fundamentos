print('Ola, escolha o seu produto para receber desconto de 5%')
preco = float(input('Digite o preço do produto:R$'))
print('-' * 15)
desconto = ( 5 * preco) / 100
precoF = preco - desconto
print('O valor do produto é: R${} \nO desconto é de: R${:.0f} \nO preço final é de: R${:.2f}'.format(preco, desconto, precoF))


