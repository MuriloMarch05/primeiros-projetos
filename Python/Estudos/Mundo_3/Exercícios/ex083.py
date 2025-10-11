# VALIDADOR DE PARÊNTESES - ESTRUTURA DE PILHA (STACK)
# Objetivo: Verificar se os parênteses estão balanceados em uma expressão

# Recebe a expressão do usuário
expr = str(input('Digite a expressão: '))

# Cria uma lista vazia que funcionará como PILHA
# Pilha = estrutura onde só adicionamos/removemos do topo (como pilha de pratos)
pilha = []

# PERCORRE CADA CARACTERE da expressão (letras, números, símbolos...)
for simb in expr:
    
    # CASO 1: Encontrou um parêntese ABRINDO '('
    if simb == '(':
        # EMPILHA (adiciona no topo da pilha)
        # Significa: "encontrei uma abertura que precisa ser fechada depois"
        pilha.append('(')
    
    # CASO 2: Encontrou um parêntese FECHANDO ')'
    elif simb == ')':
        
        # Verifica se TEM algo na pilha (se tem '(' esperando ser fechado)
        if len(pilha) > 0:
            # DESEMPILHA (remove o último '(' da pilha)
            # Significa: "esse ')' fechou um '(' que estava aberto"
            pilha.pop()
        
        # Se a pilha está VAZIA (não tem '(' para fechar)
        else:
            # ERRO! Apareceu um ')' sem ter um '(' antes
            # Adiciona ')' na pilha para indicar erro
            pilha.append(')')
            # Para o loop imediatamente
            break
    
    # Se o caractere não é '(' nem ')', simplesmente IGNORA e continua
    # (não precisa de else, pois só nos importamos com parênteses)


# VERIFICAÇÃO FINAL: Analisa o estado da pilha após processar tudo

if len(pilha) == 0:
    # Pilha VAZIA = todos os '(' foram fechados corretamente! ✅
    print('Sua expressão está válida!')

else:
    # Pilha COM elementos = erro! Pode ser:
    # - Sobraram '(' sem fechar (ex: "((a+b)")
    # - Apareceu ')' sem '(' antes (ex: "a+b)")
    print('Sua expressão está errada!')

# FIM DO PROGRAMA
