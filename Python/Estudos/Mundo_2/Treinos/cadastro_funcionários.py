# Leia nome, salário e departamento de 6 funcionários. Mostre:

# Média salarial da empresa
# Nome do funcionário mais bem pago
# Quantos funcionários ganham menos que R$ 3000

# Definindo acumuladores
media_salarial = 0
maior_salario = 0
nome_maior_salario = ''
dep_maior_salario = ''
salario_menor_de3k = 0

for s in range(1, 7): # 6 funcionários
    print(f'---------- {s} FUNCIONÁRIO ----------')
    nome = str(input('Nome: ')).strip()
    salario = float(input('Salario: R$ '))
    departamento = str(input('Departamento: ')).strip()
    media_salarial += salario # Vai acumulando o salário digitado

    if s == 1:  # Define a referência inicial
        nome_maior_salario = nome
        maior_salario = salario
        dep_maior_salario = departamento
    if salario > maior_salario: # Compara com a referência e atualiza os valores
        maior_salario = salario
        nome_maior_salario = nome
        dep_maior_salario = departamento
    if salario < 3000:  # Conta quantos recebem menos de 3k
        salario_menor_de3k += 1

media_salarial = media_salarial / 6

print(f'''A média salarial da empresa é de R${media_salarial:.1f}.
O funcionário mais bem pago é {nome_maior_salario} e ele recebe R${maior_salario} trabalhando no
departamento {dep_maior_salario} da empresa.
{salario_menor_de3k} funcionários recebem menos de R$3000.''')
