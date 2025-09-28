numero = 0
contador = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    contador += 1
    soma = soma + numero
print(f'A soma vale {soma}')
