print('''Números pares ou ímpares entre 1 e 50.
 [1]- Pares
 [2]- Ímpares''')
opcao = int(input('Escolha uma opção:'))

if opcao == 1:
    print('Os pares são:')
    for pares in range(2, 51, 2):
        print(pares, end=' ')

elif opcao == 2:
    print('Os ímpares são:')
    for impares in range(1, 51, 2):
        print(impares, end=' ')

else:
    print('Opção inválida')
