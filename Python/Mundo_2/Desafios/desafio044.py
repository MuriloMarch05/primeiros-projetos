print('='*10, 'Lojas MIL', '='*10)
preco = float(input('Preço do produto: R$'))

print('''FORMAS DE PAGAMENTO
[1]- à vista dinheiro/cheque: 10% de desconto
[2]- à vista no cartão: 5% de desconto
[3]- 2x no cartão
[4]- 3x ou mais no cartão: 20% de juros''')
escolha = int(input('Qual a forma de pagamento?'))

if escolha == 1:
    total = preco - (preco * 10 / 100)
    print(f'A sua compra de R${preco} custará R${total} com 10% de desconto!')

elif escolha == 2:
    total = preco - (preco * 5 / 100)
    print(f'A sua compra de R${preco} custará R${preco - preco * 5/100} com 5% de desconto!')

elif escolha == 3:
    total = preco
    parcela = total / 2
    print(f'A sua compra será parcelada em duas parcelas de R${parcela} e custará R${preco}')

elif escolha == 4:
    parcelas = int(input('Quantas parcelas?'))
    total = preco + (preco * 20/100)
    print(f'Sua compra de R${preco} custará R${total} e será parcelada em {parcelas}x de R${total/parcelas} com juros! ')

else:
    print('\033[31mOpção inválida.\033[m Tente novamente.')
