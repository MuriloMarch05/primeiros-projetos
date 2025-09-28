print('Gerador de Progressão Aritmética')
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))   # Solicita que o usuário escolha o início da PA
razao = int(input('Razao: '))   # Solicita a razão desejada pelo usuário
termo = primeiro
contador = 1    # Contador para limitar a quantidade de termos, inicia no 1

while contador <= 10:   # Mostra os 10 primeiros termos
    print(f'{termo} -> ', end='')
    termo += razao
    contador += 1

print('FIM')