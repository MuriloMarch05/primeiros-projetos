numero = int(input('Digite um numero inteiro:'))
escolha = int(input('[ 1 ]-Binário\n[ 2 ]-Octal\n[ 3 ]-Hexadecimal\nSua opção:'))

binario = bin(numero)[2:] # Começa a partir do terceiro caractere, retirando a identificação (0b)
octal = oct(numero)[2:] # Começa a partir do terceiro caractere, retirando a identificação (0x)
hexadecimal = hex(numero)[2:] # Começa a partir do terceiro caractere, retirando a identificação (0o)

if escolha == 1:
    print(f'O número {numero} em binário é: {binario}.')

elif escolha == 2:
    print(f'O número {numero} em octal é: {octal}.')

elif escolha == 3:
    print(f'O número {numero} em hexadecimal é: {hexadecimal}.')

else:
    print('Opção inválida. Tente novamente.')
