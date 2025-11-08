dados = dict()

nome = str(input('Nome do aluno: ')).title()
media = float(input(f'Média de {nome}: '))

dados = {
    'Nome': nome,
    'Média': media,
    'Situação': 'Aprovado' if media >= 7 else 'Reprovado'
}

print('-=' * 30)
for chave, valor in dados.items():
    print(f'{chave}: {valor}')

