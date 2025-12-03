from time import sleep

def linha():
    print('-' * 30)


def contador(i,f,p):
    print('-' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if p < 0:
        p *= -1  # Garante que o passo seja positivo
    
    if p == 0:
        p = 1  # Garante que o passo não seja zero

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.2)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.2)
            cont -= p
        print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua ver de personalizar a contagem!')


ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(ini, fim, passo)
