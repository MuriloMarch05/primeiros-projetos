print('-='*25)
print('Analisador de triângulos!')
print('-='*25)

r1 = float(input('Digite o comprimento da primeira reta:'))
r2 = float(input('Digite o comprimento da segunda reta:'))
r3 = float(input('Digite o comprimento da terceira reta:'))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Com essas retas, é possível formar um triângulo.')

else:
    print('Com essas retas, NÃO é possível formar um triângulo.')
