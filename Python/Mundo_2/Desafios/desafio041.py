from datetime import date

print('Saiba a sua categoria na natação!')

nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year

idade = ano_atual - nascimento


print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JÚNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
