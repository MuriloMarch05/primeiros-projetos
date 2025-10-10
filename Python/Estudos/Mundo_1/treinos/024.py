# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO” (ou algum que está na lista).

cid = str(input('Qual o nome da sua cidade?: ')).strip()

prefixos = ['SANTO', 'SÃO', 'SAO', 'RIO']

print(any(cid.upper().startswith(nome) for nome in prefixos ))
