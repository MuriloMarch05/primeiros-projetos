# Exercício sugerido pelo Claude, para consolidar o conceito visto nas estruturas de repetição.
# Análise de notas dos alunos.

melhor_aluno = ''
maior_media = 0
soma_medias = 0
aprovados = 0

for n in range(1, 6):
    print(f'---------- {n} ALUNO ----------')
    nome = str(input(f'Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    soma_medias += media

    if n == 1:
        maior_media = media
        melhor_aluno = nome
    if media > maior_media:
        maior_media = media
        melhor_aluno = nome
    if media >= 7:
        aprovados += 1

media_geral = soma_medias / 5

print(f'''A média geral da turma é {media_geral:.1f}.
O melhor aluno é {melhor_aluno}, com média {maior_media:.1f}.
{aprovados} alunos foram aprovados.''')
