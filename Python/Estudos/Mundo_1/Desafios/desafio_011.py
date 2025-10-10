print('Calcule quanto de tinta é necessária para sua parede!')

largura = float(input('Largura da sua parede em metros: '))
altura = float(input('Altura da sua parede em metros: '))

area = largura*altura

print(f'Sua parede tem a dimensão de {largura:.1f}x{altura:.1f} e sua área é de {area:.2f}m².')

tinta = area/2

print(f'Para pintar essa parede, você precisará de {tinta:.2f}L de tinta.')
