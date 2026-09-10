from random import randint
from time import sleep
computador=randint(0,5) #Faz o computador pensar
print('-=-'*25)
print('\033[1;30;35mVou pensar em um número inteiro entre 0 e 5. Tente adivinhar...\033[m') 
print('-=-'*25)
jogador=int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Você venceu!! Extamente o que eu pensei...')
else:
    print('Eu pensei no número {}, você perdeu!!'.format(computador))