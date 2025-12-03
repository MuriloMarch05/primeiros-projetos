def calcular_area(l, c):
    area = l*c
    print(f'A área de um terreno {l}m x {c}m é de {area:.2f}m².')


def linha():
    print('-' * 30)


linha()
print('CONTROLE DE TERRENOS'.center(30))
linha()

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

calcular_area(largura, comprimento)
linha()