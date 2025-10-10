print('Calcule o seu IMC')

peso = float(input('Digite o seu peso (Kg):'))
altura = float(input('Digite sua altura (M):'))

imc = peso / (altura**2)

if imc < 18.5:
    print(f'Abaixo do peso. Seu IMC é {imc:.1f}')

elif 18.5 <= imc <= 25:
    print(f'Peso normal. Seu IMC é {imc:.1f}')

elif 25 <= imc <= 30:
    print(f'Sobrepeso. Seu IMC é {imc:.1f}')

elif 25 <= imc <= 35:
    print(f'Obesidade grau 1. Seu IMC é {imc:.1f}')

elif 35 <= imc <= 40:
    print(f'Obesidade grau 2. Seu IMC é {imc:.1f}')

else:
    print(f'Obesidade mórbida. Seu IMC é {imc:.1f}')
