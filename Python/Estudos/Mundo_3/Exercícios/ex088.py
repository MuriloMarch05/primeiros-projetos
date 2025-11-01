from random import randint
from time import sleep

jogos = []

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))

for i in range(0, quantidade):
    jogo = []
    while len(jogo) < 6:
        numeros = randint(1, 60)
        if numeros not in jogo:
            jogo.append(numeros)
    jogos.append(jogo)

print('-=' * 3, f'SORTEANDO {quantidade} JOGOS', '-=' * 3)

for i, jogo in enumerate(jogos):
    print(f'Jogo {i + 1}: {(jogo)}')
    sleep(1)
    
