from random import shuffle
print('<<< Vai sortear uma ordem de lista randomica >>> ')
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
sorteio = shuffle(alunos)
print('a ordem randomica de apresentação foi:\n{} '.format(alunos))
