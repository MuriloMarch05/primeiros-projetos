frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split() # Separa a frase em uma lista de palavras
junto = ''.join(palavras) # Junta as palavras, retirando os espaços entre elas
inverso = ''

# Jeito mais simples, válido para o Python
# inverso = inverso[::-1]
# Dessa forma, usamos a técnica de fatiamento de strings. Excluindo o uso do for, mantendo apenas as condições.

# Jeito tradicional
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto: # Verifica se o inverso da frase é igual às palavras juntas
    print('É um palíndromo!')
else:
    print('A frase não é um palíndromo.')
