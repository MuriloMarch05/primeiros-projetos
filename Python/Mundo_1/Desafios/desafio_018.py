from math import radians, sin, cos, tan

angulo = float(input('Digite um ângulo: '))

sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print(f'O ângulo de {angulo:.0f}° tem:\nSeno de {sen:.2f}\nCosseno de {cos:.2f}\nTangente de {tan:.2f}')
