dados = dict()  # Dicionário para armazenar os dados do jogador
gols = list()   # Lista para armazenar os gols por partida
time = list()  # Lista para armazenar os dados de vários jogadores

while True:
    dados.clear()  # Limpa o dicionário dados para um novo jogador
    gols.clear()  # Limpa a lista gols para um novo jogador
    dados['nome'] = str(input('Nome do jogador: ')).title()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    for c in range(0, partidas):    # Loop para coletar os gols em cada partida
        gols.append(int(input(f'  Quantos gols na partida {c + 1}?')))

    dados['gols'] = gols[:] # Armazena uma cópia da lista gols em dados['gols']
    dados['total'] = sum(gols) # Calcula o total de gols e armazena em dados['total']
    time.append(dados.copy()) # Adiciona uma cópia do dicionário dados à lista time

    while True: # Loop para validar a resposta do usuário
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N': # Sai do loop principal se a resposta for 'N'
        break

print('-' * 40)
print('cod ', end=' ')  # Cabeçalho da tabela

for i in dados.keys():  # Cabeçalho com os nomes dos campos
    print(f'{i:<15}', end=' ')
print()

for k, v in enumerate(time):    # Dados de cada jogador
    print(f'{k:>3} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()

print('-' * 40)

while True:  # Loop para consultar os dados de um jogador específico
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')

print('<< VOLTE SEMPRE >>')

