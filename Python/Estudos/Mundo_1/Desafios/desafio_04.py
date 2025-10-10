# Lê uma entrada do usuário
valor = input('Digite algo: ')

# Mostra o tipo primitivo do valor
print('O tipo primitivo desse valor é:', type(valor))

# Mostra informações sobre o valor
print(f'Só tem espaços?', valor.isspace())
print(f'É um número?', valor.isnumeric())
print(f'É alfabético?', valor.isalpha())
print(f'É alfanumérico?', valor.isalnum())
print(f'Está em maiúsculas?', valor.isupper())
print(f'Está em minúsculas?', valor.islower())
print(f'Está capitalizada?', valor.istitle())


# Para colorir bool, é melhor usar funções. Mas no momento, ainda não aprendi. Esse exemplo peeguei do Claude.

# def colorir_bool(booleano):
#     cor = 32 if booleano else 31  # verde se True, vermelho se False
#     return f'\033[{cor}m{booleano}\033[0m'
#
# # Use em todas as linhas:
# print(f'Só tem espaços?', colorir_bool(valor.isspace()))
# print(f'É um número?', colorir_bool(valor.isnumeric()))
# print(f'É alfabético?', colorir_bool(valor.isalpha()))
# print(f'É alfanumérico?', colorir_bool(valor.isalnum()))
# print(f'Está em maiúsculas?', colorir_bool(valor.isupper()))
# print(f'Está em minúsculas?', colorir_bool(valor.islower()))
# print(f'Está capitalizada?', colorir_bool(valor.istitle()))