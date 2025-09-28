print('-+' * 25)
print('Comparador de números!')
print('-+' * 25)

num1 = float(input('Primeiro número:'))
num2 = float(input('Segundo número:'))

if num1 > num2:
    print(f'O primeiro número é maior.')

elif num2 > num1:
    print(f'O segundo número é maior.')

else:
    print('Os dois são iguais.')
