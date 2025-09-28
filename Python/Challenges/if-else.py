num = int(input("Digite um número: ").strip())

if num % 2 == 1:
    print('Weird')

elif 2 <= num <= 5:
    print('Not Weird')

elif 6 <= num <= 20:
    print('Weird')

else:
    print('Not Weird')
