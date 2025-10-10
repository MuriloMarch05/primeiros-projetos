print('-'*25)
print('Sequência de Fibonacci')
print('-'*25)
numero = int(input('Quantos números você quer mostrar?: '))
t1 = 0
t2 = 1
contador = 1
print(f'{t1} -> {t2}', end='')
while contador < numero:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    contador = contador + 1

print(' -> FIM')
print('~'*30)
