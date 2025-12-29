def fatorial(n, show=False):
    """
    -> Calcula O fatorial de um numero
    :param n: O numero a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: O valor do fatorial de um numero
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# Programa principal
print(fatorial(5, show=True))
print(fatorial(4, show=False))
