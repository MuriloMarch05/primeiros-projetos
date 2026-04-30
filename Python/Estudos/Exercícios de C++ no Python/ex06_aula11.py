# 6) Faça um programa que carregue um vetor de 15 elementos inteiros e verifique a existência de
# elementos iguais a 30, mostrando as posições em que esses elementos aparecem.


# Listas para armazenar os números e as posições dos elementos iguais a 30

numeros = []
posicoes = []

for i in range(15):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

    # Verificar se o número é igual a 30
    if num == 30:
        posicoes.append(i)

# Exibir as posições dos elementos iguais a 30

print(f"Elementos iguais a 30 encontrados nas posições: {posicoes}")
