print('-'*30)
print('Contador de números inteiros')
print('-'*30)

numero = 0
total_numeros = 0
soma_numeros = 0

while numero != 999:
    numero = int(input('Digite um número inteiro [999 para parar]: '))
    if numero != 999:
        total_numeros += 1
        soma_numeros += numero

print(f'O contador terminou, você digitou {total_numeros} números e a soma deles é {soma_numeros}. ')
