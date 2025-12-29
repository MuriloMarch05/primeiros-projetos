def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: Notas do aluno
    :param sit: Situação do aluno
    :return: Dicionário com informações do aluno
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] < 7:
            r['situacao'] = 'REPROVADO'
        if r['media'] > 7:
            r['situacao'] = 'APROVADO'
    return r



# Programa principal
resp = notas(7, 8, 9, sit=True)
print(resp)