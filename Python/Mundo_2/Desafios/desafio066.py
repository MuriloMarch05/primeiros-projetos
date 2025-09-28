print('-=-' * 25)
print('Contador de Números')
print('-=-' * 25)

total_numeros = 0
soma = 0

while True:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero == 999:
        break
    total_numeros += 1
    soma += numero

print(f'Você digitou {total_numeros} números e a soma entre eles foi {soma}.')
