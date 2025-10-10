lista_geral = []
lista_pares = []
lista_impares = []

while True:
    numeros = int(input('Digite um número: '))
    lista_geral.append(numeros)
    if numeros % 2 == 0:
        lista_pares.append(numeros)
    else:
        lista_impares.append(numeros)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
lista_geral.sort()
lista_pares.sort()
lista_impares.sort()
print('-='*30)
print(f'A lista completa é {lista_geral}\nA lista de pares é {lista_pares}\nA lista de ímpares é {lista_impares}')

