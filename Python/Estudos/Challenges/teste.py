from time import sleep

palavra = str(input('Digite uma palavra: ')).title()
print('ANALISANDO PALAVRA...')
sleep(1)
for n in palavra:
    sleep(0.2)
    print(n,end='')
