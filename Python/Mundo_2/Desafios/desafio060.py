# Faça um programa que leia um número qualquer e mostre o seu fatorial.

numero = int(input('Digite um número para calcular o seu fatorial: '))
contador = numero
fatorial = 1
print(f'Calculando {numero}!')
while contador > 0:
    print(contador, end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1

print(f'{fatorial}')

