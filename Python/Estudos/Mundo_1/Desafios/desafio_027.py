n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()

print('Prazer em te conhecer!')
print(f'Seu primeiro nome é {nome [0]}')
print(f'O seu último nome é {nome[len(nome)-1]}')
