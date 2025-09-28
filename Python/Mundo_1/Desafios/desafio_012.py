print('Calculadora de promoções!')

inicial = float(input('Digite o valor do produto: R$ '))

# 5% de desconto
desconto = inicial * 0.05

final = inicial - desconto

print(f'O produto que custava R${inicial:.2f}, na promoção com desconto de 5%, custará R${final:.2f}!')
