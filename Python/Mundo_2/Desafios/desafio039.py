from datetime import date

print('Alistamento militar!')

sexo = str(input('Digite o seu sexo: [M/F] ')).strip().upper()
if sexo == 'F':
    print('Você não precisa se alistar.')
else:
    atual = date.today().year
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc

    if idade == 18:
        print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.\nHora de se alistar!')

    elif idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.\nAinda faltam {saldo} anos para seu alistamento')
        print(f'Seu alistameno será em {ano}')

    else:
        saldo = idade - 18
        ano = atual - saldo
        print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
        print(f'Você já deveria ter se alistado há {saldo} anos.')
        print(f'Seu alistamento foi em {ano}')
