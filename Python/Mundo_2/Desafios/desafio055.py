print('Analisador de pesos')

lista_pesos = [] # Cria uma lista vazia, serve para comparar os valores posteriormente

for pesos in range(1, 6):
    peso = float(input(f'Peso da {pesos}ᵃ pessoa:'))
    lista_pesos.append(peso) # Adiciona os valores à lista para a comparação

print(f'''O maior peso foi de {max(lista_pesos)}kg.
E o menor peso foi de {min(lista_pesos)}Kg.''')
