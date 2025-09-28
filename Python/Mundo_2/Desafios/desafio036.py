print('\033[33mEmpréstimo para compra de imóveis!\033[m')

valor_casa = float(input('Qual o valor do imóvel que você deseja comprar?:\033[32mR$\033[m'))
salario = float(input('Qual é o seu salário?:\033[32mR$\033[m'))
anos = int(input('Quantos anos de financiamento?: '))
prestacao = valor_casa / (anos * 12)

if prestacao > salario * 0.3:
    print(f'\033[31mEMPRÉSTIMO NEGADO!\033[m', end='')
    print(f'O valor da prestação mensal será de R${prestacao:.2f}')

else:
    print(f'\033[32mEMPRÉSTIMO ACEITO!\033[m A prestação mensal será de R${prestacao:.2f}')
