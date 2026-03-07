print('<<< Ola, boas noticias! voce teve aumneto de salario, vamos calcular? >>>')
salario = float(input('digite seu salario: R$'))
print('-' * 15)
aumento = (15 * salario) / 100
salarioF = salario + aumento
print('salario atual é: R${:.2f} \naumento será de 15%, que corresponde a: R${:.2f} \nsalario final pós aumento é de: R${:.2f}'.format(salario, aumento, salarioF))
