times = ('Flamengo','Cruzeiro','Palmeiras','Bahia','Mirassol','Botafogo','São Paulo','Bragantino','Fluminense','Internacional'
         ,'Ceará','Corinthians','Grêmio','Atlético-MG','Vitória','Vasco','Santos','Juventude', 'Fortaleza', 'Sport')

print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)

print(f'Os cinco primeiros são: {times[0:5]}')
print('-=' * 15)

print(f'Os últimos quatro são: {times[-4:]}')
print('-=' * 15)

print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)

print(f'O time do Corinthians está na posição: {times.index('Corinthians') + 1}')
print('-=' * 15)
