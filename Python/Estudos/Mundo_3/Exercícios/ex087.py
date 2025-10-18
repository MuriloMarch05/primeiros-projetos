matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma_pares = 0
maior_segunda_linha = 0
soma_terceira_coluna = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]:'))

print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {soma_pares}')

for l in range(0,3):
    soma_terceira_coluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')

for c in range(0,3):
    if c == 0:
        maior_segunda_linha = matriz[1][c]
    elif matriz[1][c] > maior_segunda_linha:
        maior_segunda_linha = matriz[1][c]

print(f'O maior valor da segunda linha é {maior_segunda_linha}')
