# Pedindo para o usuário informar 3 números

n1 = float(input('Primeiro número:'))
n2 = float(input('Segundo número:'))
n3 = float(input('Terceiro número:'))

# Verificando qual é o menor
menor = min(n1, n2, n3)

# Verificando qual é o maior
maior = max(n1, n2, n3)

# Mostrando na tela
print(f'O menor número é {menor:.1f} e o maior número é {maior:.1f} ')