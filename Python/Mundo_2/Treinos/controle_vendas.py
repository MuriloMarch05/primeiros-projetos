# Leia nome do vendedor, valor da venda e região de 4 vendedores. Calcule:

# Total de vendas da empresa
# Nome do vendedor que mais vendeu
# Quantas vendas foram acima de R$ 5000

# Definir acumuladores
total_vendas = 0
nome_mais_vendeu = ''
total_maisvendas = 0
vendas_5k = 0
regioes = ''

for v in range(1, 5): # 4 funcionários
    print(f'---------- VENDEDOR {v} ----------')
    nome = str(input('Nome: ')).strip()
    valor_venda = float(input('Valor da venda: R$'))
    regiao = str(input('Região: ')).strip()
    total_vendas += valor_venda # Acumula o total de vendas

    if v == 1:  # Toma o primeiro como referência
        nome_mais_vendeu = nome
        total_maisvendas = valor_venda
        regioes = regiao
    if valor_venda > total_maisvendas:  # Compara com a referência e atualiza
        nome_mais_vendeu = nome
        total_maisvendas = valor_venda
        regioes = regiao
    if valor_venda > 5000:  # Analisa os valores digitados e mostra quandos correspondem à condição
        vendas_5k += 1

print(f'''O total de vendas da empresa foi de R${total_vendas:.2f}.
O vendedor que mais vendeu foi {nome_mais_vendeu}, que vendeu R${total_maisvendas:.2f} na região de {regioes}.
A empresa obteve {vendas_5k} vendas acima de R$5000''')
