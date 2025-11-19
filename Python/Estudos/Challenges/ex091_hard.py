from random import randint

jogadores = ['jogador-1', 'jogador-2', 'jogador-3','jogador-4']

resultados = dict()

for jogador in jogadores:
    resultados[jogador] = randint(1, 6)

print('-=' * 20)
print('=> VALORES SORTEADOS <='.center(40))
print('-' * 40)

for j, r in resultados.items():
    print(f'O {j} tirou {r} no dado.')

print('-' * 40)
print('=> RANKING DOS JOGADORES <='.center(40))
print('-' * 40)

rank = sorted(resultados.items(), key=lambda item: item[1], reverse=True)

for posicao, (j, r) in enumerate(rank):
    print(f'{posicao + 1}º lugar: {j} com {r} pontos.')

print('-=' * 20)
