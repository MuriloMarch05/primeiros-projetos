# Transformar o valor em número inteiro

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2

cores = {'limpa':'\033[m', 'amarelo':'\033[33m', 'azul':'\033[34m', 'verde':'\033[32m'}

print(f'{cores['amarelo']}{num1}{cores['limpa']} + {cores['azul']}{num2}{cores['limpa']} = {cores['verde']}{soma}{cores['limpa']}')
