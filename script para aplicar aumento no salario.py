print('<<< Ola, boas noticias! voce teve aumneto de salario, vamos calcular? >>>')
salario = float(input('digite seu salario: R$'))
aumento = (15 * salario) / 100
salarioF = salario + aumento
print('salario atual é: R${:.0f} \naumento sera de: R${:.0f} \nsalario final pos aumneto é de: R${:.0f}'.format(salario, aumento, salarioF))