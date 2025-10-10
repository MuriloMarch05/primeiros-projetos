"""Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('-' * 25)
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    print('-' * 25)
    opcao = int(input('>>>>> Qual é a sua opção?: '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}.')
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f'O produto entre {n1} e {n2} é {multiplicar}. ')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'O maior valor entre {n1} e {n2} é {maior}.')
        elif n1 == n2:
            print(f'Os números {n1} e {n2} são iguais.')
        else:
            maior = n2
            print(f'O maior número entre {n1} e {n2} é {maior}.')
    elif opcao == 4:
        print('Informe os valores novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida. Tente novamente.')
    sleep(2)
print('Fim do programa. Volte sempre!')
