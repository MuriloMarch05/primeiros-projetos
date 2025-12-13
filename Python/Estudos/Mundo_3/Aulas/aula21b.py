def fatorial(num=1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f

n = int(input('Digite um número para saber seu fatorial: '))
print(f'O fatorial de {n} é igual a {fatorial(n)} ')

def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False

numero = int(input('Digite um valor para saber se é par: '))
if par(numero):
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} não é par.')
