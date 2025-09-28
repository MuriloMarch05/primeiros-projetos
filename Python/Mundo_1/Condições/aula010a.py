n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua média foi {media:.1f}.')
if media >= 7:
    print('Você passou! Parabéns!')

else:
    print('Você não passou. Que pena!')