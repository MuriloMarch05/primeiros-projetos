from time import sleep
import emoji


print('Fogos de artifício!')

for fogos in range(10, -1, -1):
    print(fogos)
    sleep(1)

print('BOOM!!! POW!! POW!!', emoji.emojize(':fireworks:'))
