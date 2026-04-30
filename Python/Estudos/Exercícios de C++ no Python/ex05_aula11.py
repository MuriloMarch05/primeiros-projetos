#5) Elabore um programa que carregue um vetor de seis elementos numéricos inteiros, calcule e
#mostre:
#a quantidade de números pares;
#quais os números pares;
#a quantidade de números ímpares;
#quais os números ímpares;

# Listas para armazenar os números, os pares e os ímpares
numeros = []
pares = []
impares = []


for i in range(6):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

    # Verificar se o número é par ou ímpar
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Exibir os resultados
print(f"Quantidade de números pares: {len(pares)}")
print(f"Números pares: {pares}")
print(f"Quantidade de números ímpares: {len(impares)}")
print(f"Números ímpares: {impares}")
