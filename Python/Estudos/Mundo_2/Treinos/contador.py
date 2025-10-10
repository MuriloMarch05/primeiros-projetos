# Faça um programa que conte de um número inicial até um número final, 
# permitindo ao usuário escolher de quanto em quanto vai contar.

print('Contador de números')
print('-='*10)

primeiro = int(input('Número inicial: '))
ultimo = int(input('Número final: '))
passo = int(input('De quanto em quanto você quer contar?: '))

contador = primeiro

while contador <= ultimo:
    print(f'{contador}', end='')
    contador += passo
    if contador <= ultimo:
        print('->', end='')

print(' FIM')
