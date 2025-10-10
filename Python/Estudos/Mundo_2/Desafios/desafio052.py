num = int(input('Digite um número: '))
tot = 0 # Total de números divisíveis

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end=' ')
        tot += 1 # Mesmo que tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')

print(f'\n\033[mO número {num} foi divisível {tot} vezes.')
if tot == 2:
    print('Portanto, ele é um número PRIMO.')
else:
    print('Portanto, ele não é um número PRIMO.')
