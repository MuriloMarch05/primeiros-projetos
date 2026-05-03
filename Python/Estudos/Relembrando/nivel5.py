def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
maior_numero(a, b)
print(f'O maior numero é {maior_numero(a, b)}.')
