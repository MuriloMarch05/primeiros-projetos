print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 -1) * razao # Fórmula do termo geral em uma PA

for pa in range(primeiro, decimo, razao):
    print(pa, end=' ⭢ ')
print('ACABOU')
