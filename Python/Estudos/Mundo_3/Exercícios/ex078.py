valores = []    # Lista vazia

for c in range(0, 5):   # Contador
    valores.append(int(input(f'Digite um valor para a posição {c}: '))) # Adiciona os números digitados à lista

maior = max(valores)    # Maior número digitado
menor = min(valores)    # Menor número digitado

#   Encontrar TODAS as posições do maior valor
posicoes_maior = [i for i, v in enumerate(valores) if v == maior]

# Encontrar TODAS as posições do menor valor
posicoes_menor = [i for i, v in enumerate(valores) if v == menor]

# Mostra a lista completa
print('-='*30)
print(f'Você digitou os elementos: {valores}')

# Mostra a quantidade de elementos
print(f'A lista tem {len(valores)} elementos.')

# Mostra todas as posições do maior valor
if len(posicoes_maior) == 1:
    print(f'O maior valor digitado foi {maior} na posição {posicoes_maior[0]}.')
else:
    print(f'O maior digitado foi {maior} nas posições {posicoes_maior}.')

# Mostra todas as posições do menor valor
if len(posicoes_menor) == 1:
    print(f'O menor valor digitado foi {menor} na posição {posicoes_menor[0]}.')

else:
    print(f'O menor valor digitado foi {menor} nas posições {posicoes_menor}.')

print('-='*30)
print('ORDEM CRESCENTE'.center(60))
ordem = sorted(valores)
print(f'{ordem}'.center(60))
print('-='*30)
print('ORDEM DECRESCENTE'.center(60))
ordem = sorted(valores, reverse=True)
print(f'{ordem}'.center(60))
print('-='*30)
