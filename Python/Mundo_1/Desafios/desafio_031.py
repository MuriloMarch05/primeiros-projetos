distancia = float(input('Qual a distância da sua viagem em Km?:'))

print(f'Você está prestes a começar uma viagem de {distancia} km!')

if distancia <= 200:
    valor = distancia * 0.50

else:
    valor = distancia * 0.45

print(f'E a sua passagem custará R$ {valor:.2f}')