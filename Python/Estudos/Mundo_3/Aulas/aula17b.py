valores = list()

for cont in range(0,3):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}!')

print('Fim da lista.')
print(f'A lista tem {len(valores)} elementos.')
