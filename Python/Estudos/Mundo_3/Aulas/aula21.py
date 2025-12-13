# Interative help
# Docstrings
# Argumentos opcionais
# Escopo de variáveis
# Retorno de resultados
from time import sleep


def linha():
    print('-'*30)

#-----------------------------------------------
# DOCSTRING

def somar(a=0, b=0 , c=0):
    """
    -> Faz a soma entre 3 números.
    :param a: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')

help(somar)
somar(10,15,20)
somar(10, 5)
somar(10)
somar()

#-----------------------------------------------
linha()

# DOCSTRING

def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        sleep(0.3)
        print(f'{c} -> ', end='', flush=True)
        c += p
    print('FIM')


help(contador)
contador(0,100,10)

#----------------------------------------------
linha()

# ESCOPO DE VARIÁVEIS

def funcao():
    global n1
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')

#---------------------------------------------
linha()

# RETORNO DE RESULTADOS

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(1,2,3)
r2 = somar(4,5,6)
r3 = somar(7,8,9)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')
