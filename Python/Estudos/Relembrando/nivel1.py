def verificar_maioridade(idade):
    if idade >= 18:
        print('Você é maior de idade.')
    else:
        print('Você é menor de idade.')
        

def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar')


nome = input('Digite seu nome: ').strip().title()
idade = int(input('Digite sua idade: '))

print(f'Olá, {nome}! Você tem {idade} anos.')

verificar_maioridade(idade)  

numero = int(input('Digite um número inteiro: '))
par_ou_impar(numero)
