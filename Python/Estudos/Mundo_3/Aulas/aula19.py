estado = dict()
brasil = list()

for c in range (0,3):
    estado['UF'] = str(input('Unidade Federativa: ')).title()
    estado['sigla'] = str(input('Sigla: ')).strip().upper()
    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    for k, v in e.items():
        print(v, end = ' ')
    print()

