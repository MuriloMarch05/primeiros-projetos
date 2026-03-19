print('-' * 30)
print('CADASTRO DE PRODUTOS'.center(30))
print('-' * 30)

produtos = []

for i in range(3):
    nome = input('Digite o nome do produto: ').strip().title()
    preco = float(input('Preço do produto: '))
    produtos.append([nome, preco])

for p in produtos:
    print('-'*30)
    print(f'{p[0]} - R${p[1]}')





