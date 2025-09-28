# Resumo feito com o Claude, apenas para lembrar.
#------------------------------------------------
# Indexação (acessar posições específicas)

texto = "Python"
#        012345  (índices positivos)
#       -654321  (índices negativos)

print(texto[0])   # P (primeira letra)
print(texto[2])   # t
print(texto[-1])  # n (última letra)
print(texto[-2])  # o (penúltima)

# Slicing (fatias/pedaços da string)

texto = "Python"

print(texto[1:4])    # yth (do índice 1 até 3)
print(texto[:3])     # Pyt (do início até índice 2)
print(texto[2:])     # thon (do índice 2 até o fim)
print(texto[::2])    # Pto (pula de 2 em 2)
print(texto[::-1])   # nohtyP (inverte a string)

# Métodos mais comuns

nome = "João Silva"

print(nome.upper())  # JOÃO SILVA
print(nome.lower())  # joão silva
print(nome.capitalize())  # João silva
print(nome.title()) # João Silva
print(nome.strip())  # Remove espaços
print(nome.replace('Silva', 'Python')) # João Python
print("Silva" in nome)  # True
print(len(nome))  # Conta os espaços

# count() - conta quantas vezes algo aparece

texto = "Python é uma linguagem legal"

print(texto.count("Python"))    # 1 (aparece 1 vez)
print(texto.count("a"))         # 4 (letra 'a' aparece 4 vezes)
print(texto.count("java"))      # 0 (não aparece)

# É case-sensitive (diferencia maiúscula/minúscula)
print(texto.count("python"))    # 0 (com 'p' minúsculo)

# find() - encontra a posição da primeira ocorrência

texto = "Python é uma linguagem Python"

print(texto.find("Python"))     # 0 (primeira ocorrência no índice 0)
print(texto.find("é"))          # 7 (encontra no índice 7)
print(texto.find("uma"))        # 9 (encontra no índice 9)
print(texto.find("java"))       # -1 (não encontrou, retorna -1)

# Para encontrar a partir de uma posição específica
print(texto.find("Python", 1))  # 25 (procura a partir do índice 1)