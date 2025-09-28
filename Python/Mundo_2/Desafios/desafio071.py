print('=' * 30)
print('{:^30}'.format('BANCO DO BOM'))
print('=' * 30)

valor = int(input('Quanto você quer sacar? R$'))
total = valor
cedula = 50
totalcedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        totalcedulas += 1
    else:
        # Se usou pelo menos uma cédula dessa denominação, mostra o resultado
        if totalcedulas > 0:
            print(f'Total de {totalcedulas} cédulas de R$ {cedula}.')

        # Passa para a próxima menor cédula
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        elif cedula == 1:
            # Não há mais cédulas menores, encerra o programa
            break

        # Zera o contador para a nova denominação
        totalcedulas = 0

print('=' * 30)
print('Volte sempre ao BANCO DO BOM!')
print('=' * 30)
