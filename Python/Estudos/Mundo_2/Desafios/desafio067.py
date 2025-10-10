while True:
    numero = int(input('Você quer ver a tabuada de qual número?: '))
    if numero < 0:
        break
    print('-' * 30)
    for tabuada in range(1, 11):
        print(f'{numero} x {tabuada:2} = {numero * tabuada}')
    print('-' * 30)
print('Programa de tabuada encerrado.')
