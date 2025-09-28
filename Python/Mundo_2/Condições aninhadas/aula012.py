nome = str(input('Qual é o seu nome?:')).strip()

if nome.upper().startswith('MURILO'):
    print('Que nome bonito!')

elif nome.upper() in 'JOAO, JOÃO, MARIA, PEDRO':
    print('Seu nome é bem popular no Brasil.')

else:
    print('Seu nome é normal.')

print(f'Prazer em te conhecer {nome.title()}!')
