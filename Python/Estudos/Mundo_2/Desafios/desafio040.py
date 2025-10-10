print('Calcule sua média!')

p1 = float(input('Digite sua primeira nota: '))
p2 = float(input('Digite sua segunda nota: '))
media = (p1+p2) / 2

if media >= 7:
    print(f'Tirando {p1:.1f} e {p2:.1f}, a média do aluno é {media:.1f}.\nO aluno está \033[32mAPROVADO\033[m')

elif media >= 5 < 7:
    print(f'Tirando {p1:.1f} e {p2:.1f}, a média do aluno é {media:.1f}.\nO aluno está de \033[33mRECUPERAÇÃO\033[m')

else:
    print(f'Tirando {p1:.1f} e {p2:.1f}, a média do aluno é {media:.1f}.\nO aluno está \033[31mREPROVADO\033[m')
