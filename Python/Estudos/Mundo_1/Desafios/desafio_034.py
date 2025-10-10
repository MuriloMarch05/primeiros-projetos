salario = float(input('Qual é o salário atual?:R$'))

if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)

print(f'Quem recebia R${salario} passa a receber R${novo:.2f} a partir de agora.')