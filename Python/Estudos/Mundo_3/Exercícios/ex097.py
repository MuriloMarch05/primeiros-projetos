def escrever(txt):
    tamanho = len(txt) + 4    
    print('~' * tamanho)
    print(f'  {txt}')
    print('~' * tamanho)

# Programa Principal
escrever('Curso em Vídeo')
escrever('Aprenda Python 3')
escrever('CeV')
escrever('Funções são legais!')
