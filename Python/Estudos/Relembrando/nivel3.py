nomes = list()

for i in range(4):
    nome = input('Digite um nome: ').title().strip()
    nomes.append(nome)

nomes.sort()
print(f'Os nomes digitados foram {nomes} em ordem alfabética.')

#--------------------------------------------------------------------

numeros = list()

for f in range(6):
    num = int(input('Digite um numero: '))
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)
maiores_media = 0

for n in numeros:
    if n > media:
        maiores_media += 1


print(f'Voce digitou os numeros {numeros}.\nO maior é o numero {maior}, o menor é {menor}, a media é {media} e ao todo, temos {maiores_media} numeros maiores que a media.')