# Ver tabuada de um número

num = int(input('Digite um número para ver sua tabuada: '))

for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')

#------------------------------------------------------------

# Testar senhas

senha = 'python123'
tentativas = 0

while True:

    tentar = input('Digite a senha: ')

    if tentar == senha:
        break
    else:
        print('Senha errada. Tente novamente.')

    tentativas += 1

print(f'Desbloqueado. Você tentou {tentativas} vezes')

#-----------------------------------------------------------

# Contador e acumulador

todos = list()
contador = 0
pares = 0
impares = 0

while contador < 5:
    number = int(input('Digite um numero: '))
    todos.append(number)
    contador += 1

    if number % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Você digitou os números {todos}. Ao todo, temos {pares} pares e {impares} ímpares.')