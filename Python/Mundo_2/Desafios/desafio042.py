print('-='*25)
print('Analisador de triângulos!')
print('-='*25)

# Leitura dos lados de um Triângulo
r1 = float(input('Comprimento da primeira reta:'))
r2 = float(input('Comprimento da segunda reta:'))
r3 = float(input('Comprimento da terceira reta:'))

# Condição para que se possa formar um triângulo e o seus 3 tipos
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Com essas retas, é possível formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('Com essas retas, NÃO é possível formar um triângulo.')
