vel = float(input('Qual é a velocidade atual do carro?: '))
multa = (vel - 80) * 7

if vel > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h\nA multa custará R${multa:.2f}!')
else:
    print('Você está dentro do limite permitido!.')

print('Tenha um bom dia! Dirija com segurança.')