lista = []
cinco = 0

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n == 5:
        cinco += 1
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break

lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'A lista completa é {lista}.')
print(f'O número 5 faz parte da lista e apareceu {cinco} vezes.')
print(f'Os valores em ordem decrescente são {lista}')
