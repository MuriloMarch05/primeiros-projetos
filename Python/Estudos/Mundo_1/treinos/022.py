#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: ')).strip()
separa = nome.split()

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}.\nSeu nome em minúsculas é {nome.lower()}.\nSeu primeiro nome é {separa[0]} e tem {len(separa[0])} letras.\nSeu último nome é {separa[-1]} e tem {len(separa[-1])} letras')
