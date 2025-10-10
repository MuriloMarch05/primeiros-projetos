from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

escolha = int(input('Em qual número eu pensei?'))
num = randint(0,5)
print('PROCESSANDO...')
sleep(3)

if escolha == num:
    print('Você acertou! Parabéns!')
else:
    print(f'Você errou! O número era {num}.')
