from time import sleep

lista = []

while True:
    num = int(input('Digite um número para a lista: '))
    
    if num in lista:
        print('Esse número já está na lista. Digite outro.') 
    else:
        lista.append(num)
        sleep(0.5)
        print('Número adicionado com sucesso.')

    escolha = input('Quer continuar? S/N ').upper()
    if escolha in 'Nn':
        break

sleep(2)
lista.sort()
print('-'*60)
print(f'Programa finalizado. A lista é: {lista}')

