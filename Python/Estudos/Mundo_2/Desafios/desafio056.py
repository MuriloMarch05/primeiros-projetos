somaidade = 0   # Vai somar todas as idades para calcular a média
media = 0   # Vai guardar a média final
maioridadehomem = 0 # Maior idade encontrada entre os homens
nomevelho = ''  # Nome do homem mais velho
totmulher20 = 0 # Contador de mulheres com menos de 20 anos

for p in range(1, 5):
    print(f'---------- {p}ᵃ PESSOA ----------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade  # Vai acumulando as idades
    # PRIMEIRA VERIFICAÇÃO - se é a primeira pessoa e é homem
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade # Define ele como referência inicial
        nomevelho = nome
    # SEGUNDA VERIFICAÇÃO - se é homem e tem idade maior que a atual maior
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade # Atualiza para a nova maior idade
        nomevelho = nome    # Atualiza para o novo nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1 # Soma +1 no contador

media = somaidade / 4
print(f'A média de idade do grupo é {media} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo, são {totmulher20} mulheres com menos de 20 anos.')
