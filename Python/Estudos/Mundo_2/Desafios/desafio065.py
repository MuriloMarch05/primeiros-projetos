continuar = 'S'
total_numeros = 0
soma = 0
maior = 0
menor = 0
contador = 0

while continuar in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    total_numeros += 1
    contador += 1
    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

media = soma / total_numeros
print(f'''Você digitou {total_numeros} números e a média foi {media}.
O maior valor foi {maior} e o menor foi {menor}.''')
