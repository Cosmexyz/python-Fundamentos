import random
print('<<< Vamos sortea um aluno >>>')
aluno1 = input('Primeiro aluno: ')
aluno2 = input('segundo aluno: ')
aluno3 = input('terceiro aluno: ')
aluno4 = input('quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
print('o sorteado foi: {}'.format(random.choice(alunos)))