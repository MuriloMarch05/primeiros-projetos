# Introdução às tuplas

lanche = ('Hambúrguer','Suco','Pizza','Pudim') # Tuplas são imutáveis

print(lanche)

print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])

print(lanche[1:3])

for comida in lanche:   # Caso não precise da posição, maneira mais simples
    print(f'Eu vou comer {comida}.')

for cont in range(0, len(lanche)):  # Caso eu precise da posição, usando len.
    print(f'Eu vou comer {lanche[cont]}.')

for pos, comida in enumerate(lanche):   # Caso eu precise da posição, usando enumerate.
    print(f'Eu vou comer {comida} na posicao {pos}.')
