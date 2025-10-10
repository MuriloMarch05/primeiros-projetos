homens = 0
mulheres_menos_20 = 0
total_18 = 0
while True:
    print('-' * 30)
    print('CADASTRO DE PESSOAS')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        total_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'''Total de pessoas com 18 anos: {total_18}
Ao todo, temos {homens} homens cadastrados.
E ainda, temos {mulheres_menos_20} mulheres com menos de 20 anos.''')
