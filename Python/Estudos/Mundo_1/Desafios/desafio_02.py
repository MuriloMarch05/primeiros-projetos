dia = input('Dia: ')
mes = input('Mes: ')
ano = input('Ano: ')

cores = {'limpa':'\033[m', 'verde':'\033[0;32m', 'amarelo':'\033[33m', 'azul':'\033[34m'}

print(f'Você nasceu no {cores['azul'] + dia + cores['limpa']} de {cores['amarelo'] + mes + cores['limpa']} de {cores['verde'] + ano + cores['limpa']}. Correto?')
