dados = dict()
pessoas = list()
soma = 0 
media = 0

while True:

    dados.clear()
    dados['nome'] = input('Nome: ').title().strip()
    while True:
        dados['sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())

    while True:
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break

media = soma / len(pessoas)
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram:', end=' ')

for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()

print('D) Lista das pessoas que estão acima da média:')

for p in pessoas:
    if p['idade'] > media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
        
print('-' * 30)       
print('<< ENCERRADO >>')