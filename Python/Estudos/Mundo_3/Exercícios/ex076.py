listagem = ('Teclado', 150,
            'Mouse', 90,
            'Monitor', 650,
            'Gabinete', 200,
            'Fonte', 400,
            'Placa de vídeo', 1500)

print('-'*40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-'*40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:.2f}')

print('-'*40)
