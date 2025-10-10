print('Conversor de unidades de medida!')

metros = float(input('Digite o valor em metros: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros*10
cm = metros*100
mm = metros*1000

print(f'O valor de {metros} metros é igual a: \n{km}km \n{hm}hm \n{dam}dam \n{dm}dm \n{cm}cm \n{mm}mm.')