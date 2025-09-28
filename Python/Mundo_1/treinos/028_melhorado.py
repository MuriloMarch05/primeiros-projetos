from random import randint
from time import sleep

def jogar_adivinhacao():
    while True:  # Loop principal (repetir o jogo)
        print('--' * 25)
        print('Pensei em um número entre 0 e 5. Tente adivinhar!')
        print('--' * 25)

        try:
            escolha = int(input('Em qual número eu pensei? '))
            num = randint(0, 5)  # Corrigido: randint(0, 5) sem "a:" e "b:"
            print('PROCESSANDO...')
            sleep(2)  # Tempo dramático antes do resultado

            if escolha == num:
                print('Você acertou! Parabéns! 🎉')
            else:
                print(f'Você errou! O número era {num}. 😢')

        except ValueError:  # Se o usuário não digitar um número
            print('Por favor, digite um número válido!')

        # Pergunta se quer jogar novamente
        repetir = input('Quer jogar de novo? (S/N) ').strip().upper()
        if repetir != 'S':
            print('Até mais! Obrigado por jogar. 👋')
            break  # Encerra o loop

# Inicia o jogo
if __name__ == "__main__":
    jogar_adivinhacao()