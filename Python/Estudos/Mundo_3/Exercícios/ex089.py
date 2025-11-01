from time import sleep

alunos = [] # Lista vazia

# Coleta de dados
while True:
    nome = str(input('Nome: ')).title().strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    continuar = str(input('Deseja continuar? [S/N] ').strip().upper()[0])
    if continuar in 'Nn':
        break

# Tabela
print(alunos)
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

# Para cada aluno, mostra: posição (i), nome (a[0]) e média (a[2])
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

# 'Loop' para verificar notas individualmente
while True:
    opc = int(input(f'Deseja ver as notas de qual aluno? (999 para parar) '))
    if opc == 999:
        texto = 'FINALIZANDO...'
        for letra in texto:
            print(letra, end='', flush=True)
            sleep(0.2)
        print()  # Pula linha
        break

    if opc <= len(alunos) - 1:  # Verifica se o índice existe (válido de 0 até quantidade-1)
        print(f'Notas de {alunos[opc][0]}: {alunos[opc][1]}')   # [opc] = aluno escolhido, [0] = nome, [1] = lista de notas
    else:
        print('Aluno não encontrado! Tente novamente.') # Caso o índice seja inválido, tenta novamente.

# Mensagem final
print('<<< VOLTE SEMPRE >>>')
