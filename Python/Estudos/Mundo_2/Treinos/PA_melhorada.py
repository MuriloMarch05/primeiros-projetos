print('PA avançada')
print('-='*10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
contador = 1
total = 0   # Contador pra calcular quantos termos foram mostrados no total
mais = 10   # Serve para que o usuário escolha quantos termos ele quer a mais

while mais != 0:    # Caso o usuário digite 0, o programa finaliza.
    total += mais
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))

print(f'Progressão finalizada. Foram {total} termos mostrados. ')
