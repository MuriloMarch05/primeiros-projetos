from random import randint
from time import sleep

print('-=' * 10)
print('\033[32mJOKENPO\033[m') # Título do programa
print('-=' * 10)

itens = ('Pedra', 'Papel', 'Tesoura') # Lista de opções
computador = randint(0,2) # Randomiza escolhas
print('''Suas opções:
[0]- PEDRA
[1]- PAPEL
[2]- TESOURA''')
jogador = int(input('Qual é a sua jogada?')) # Jogador escolhe uma opção

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('='*22)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('='*22)

if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida.')

elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida')

elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida.')
