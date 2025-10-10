import random

print('Sorteio de nomes e ordem de apresentação!')

aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)

print(f'A ordem de apresentação será:\n{alunos}')
