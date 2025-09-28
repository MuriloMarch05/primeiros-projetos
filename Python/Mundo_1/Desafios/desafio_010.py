print('Conversor de moedas!')

reais = float(input('Quanto dinheiro você tem na carteira? R$'))

dolares = reais / 5.56
euros = reais / 6.47
ienes = reais / 0.037
libra = reais / 7.46

print(f'Com R${reais:.2f} você pode comprar U${dolares:.2f}, €{euros:.2f}, ¥{ienes:.2f} e £{libra:.2f}. ')
