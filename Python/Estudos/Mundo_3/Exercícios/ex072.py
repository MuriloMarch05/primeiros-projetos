from time import sleep

print('-' *30)
print('NÚMEROS POR EXTENSO'.center(30))
print('-' *30)

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez')

contador = 0    # Contar quantas vezes o usuário digitou algum número.
historico = []

while True:
    # Loop para validar o número
    while True:
        escolha = int(input('Digite um número entre 0 e 10: '))
        if 0 <= escolha <= 10:
            break
        print('Número inválido. ', end='')
    contador += 1
    historico.append(escolha)
    print(f'Você digitou o número {numeros[escolha]}.')

    # Pergunta se quer continuar
    continuar = input('Deseja continuar? (S/N): ').upper()[0]

    if continuar != 'S':
        break

sleep(1)
print(f'Programa encerrado! Você digitou {contador} números no total, e eles foram: {historico}')


'''┌─── while True (EXTERNO) ───┐
│                            │
│  ┌─── while True (INTERNO) ─┐
│  │  Pede número            │
│  │  Número válido?         │
│  │  Se não → continua loop │
│  │  Se sim → break         │
│  └─────────────────────────┘
│                            │
│  Mostra resultado          │
│  Quer continuar?           │
│  Se não → break            │
│  Se sim → volta ao início  │
└────────────────────────────┘'''