from datetime import date

dados = dict()

dados['Nome'] = str(input('Nome: ')).title()
nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
dados['Idade'] = ano_atual - nascimento
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem):'))

if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentatoria'] = dados['Idade'] + (dados['contratação'] + 35) - ano_atual

print('-=' * 30)

for k, v in dados.items():
    print(f' - {k} tem valor {v}')
