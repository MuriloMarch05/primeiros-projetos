from math import hypot

co = float(input('Qual o comprimento do cateto oposto?: '))
ca = float(input('Qual o comprimento do cateto adjacente?: '))

hi = hypot(co, ca)

print(f'Os catetos são {co:.0f} e {ca:.0f}')
print(f'A hipotenusa desse triângulo vale {hi:.2f}')