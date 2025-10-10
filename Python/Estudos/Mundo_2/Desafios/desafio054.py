from datetime import date

print('Grupo da Maioridade')

atual = date.today().year
totmaior = 0
totmenor = 0

for pessoas in range(1, 8):
    nascimento = int(input(f'Em que ano a {pessoas}ᵃ pessoa nasceu? '))
    idade = atual - nascimento
    if idade >= 18:
        totmaior += 1
    else:
       totmenor += 1

print(f'''Ao todo tivemos {totmaior} pessoas maiores de idade. 
E também tivemos {totmenor} pessoas menores de idade.''')
