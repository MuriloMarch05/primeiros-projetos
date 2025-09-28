# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('-' * 30)
print('LOJÃO DO BÃO'.center(25))
print('-' * 30)

total_gasto = 0
produto_1000 = 0
mais_barato = 0
produto_barato = ' '
contador = 0

while True:
    nome_produto = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Preço: R$'))
    contador += 1
    total_gasto += preco

    if preco > 1000:
        produto_1000 += 1
    if contador == 1:
        mais_barato = preco
        produto_barato = nome_produto
    else:
        if preco < mais_barato:
            mais_barato = preco
            produto_barato = nome_produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'''O total da compra foi R${total_gasto}.
{produto_1000} produtos custam mais de R$ 1000,00.
O produto mais barato é {produto_barato} e ele custa R${mais_barato}.''')
