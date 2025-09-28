# nome = input('Qual é o seu nome?:')
# print(f'Prazer em te conhecer {nome:-^20}!')


n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
dint = n1 // n2
e = n1 ** n2
print(f'A soma é {n1+n2}, o produto é {mult} e a divisão é {div:.1f} ', end='')
print(f'divisão inteira é {dint} e a potência é {e}')

