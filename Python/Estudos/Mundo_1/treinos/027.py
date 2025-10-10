# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()

separa = nome.split()

print(f'Seu primeiro nome é {separa[0].capitalize()} e o seu último nome é {separa[-1].capitalize()}.')

