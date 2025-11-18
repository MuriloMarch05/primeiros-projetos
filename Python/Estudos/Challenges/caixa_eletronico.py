# Simulador de Caixa Eletrônico simples

valor = int(input('Valor para saque: R$ ')) # Solicita o valor do saque ao usuário

for nota in [200, 100, 50, 20, 10, 5, 2]:   # Define as cédulas disponíveis

    qtd = valor // nota # Calcula a quantidade de cédulas daquela denominação

    if qtd: # Se a quantidade for maior que zero, imprime o resultado

        print(f'Total de {qtd} notas de R$ {nota}')
        
    valor %= nota   # Atualiza o valor restante para saque
