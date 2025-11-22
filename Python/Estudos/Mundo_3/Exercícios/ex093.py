dados = dict()  # Dicionário para armazenar os dados do jogador
gols = list()   # Lista para armazenar os gols por partida

dados['nome'] = str(input('Nome do jogador: ')).title()
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for c in range(0, partidas):    # Loop para coletar os gols em cada partida
    gols.append(int(input(f'  Quantos gols na partida {c + 1}?')))

dados['gols'] = gols[:] # Armazena uma cópia da lista gols em dados['gols']
dados['total'] = sum(gols) # Calcula o total de gols e armazena em dados['total']
media = dados['total'] / partidas if partidas > 0 else 0 # Calcula a média de gols por partida

print('-=' * 30)
print(dados)
print('-=' * 30)

for k, v in dados.items():  # Itera sobre os itens do dicionário dados
    print(f'O campo {k} tem valor {v}.')

print('-=' * 30)

print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(dados['gols']):   # Itera sobre a lista de gols com índice
    print(f'  => Na partida {i + 1}, {dados["nome"]} fez {v} gols.')

print('-=' * 30)
print('RESUMO DO JOGADOR'.center(60))
print('-=' * 30)
print(f'NOME: {dados["nome"]}\nPARTIDAS: {partidas}\nTOTAL DE GOLS: {dados["total"]}\nMÉDIA DE GOLS POR PARTIDA: {media:.1f}')
