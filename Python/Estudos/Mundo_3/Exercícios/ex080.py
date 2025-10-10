lista = []

for n in range(0, 5):
    numeros = int(input('Digite um número: '))
    if n == 0 or numeros > lista[-1]:
        lista.append(numeros)
        print('Adicionando ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if numeros <= lista[pos]:
                lista.insert(pos, numeros)
                print(f'Adicionando na posição {pos} da lista...')
                break
            pos += 1

print('-='*50)
print(f'Os valores digitados em ordem foram {lista}')
