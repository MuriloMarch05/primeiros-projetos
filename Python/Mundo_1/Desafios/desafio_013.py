print('Saiba o seu novo salário!')

atual = float(input('Qual é o seu salário atual?:R$'))

aumento = atual * 0.15

novo = atual + aumento

print(f'Seu novo salário é R${novo:.2f}.')
