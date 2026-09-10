from time import sleep
from random import randint
itens=('Pedra','Papel','Tesoura')
computador=randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador=int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador==0:#Computador jogou PEDRA
    if jogador==0:
        print('EMPATE')
    elif jogador==1:
        print('JOGADOR VENCEU')
    elif jogador==2:
        print('COMPUTADOR VENCEU')
    else:
        print('\033[1;31mComando inválido')
elif computador==1:#Computador jogou PAPEL
    if jogador==0:
        print('COMPUTADOR VENCEU')
    elif jogador==1:
        print('EMPATE')
    elif jogador==2:
        print('JOGADOR VENCEU')
    else:
        print('\033[1;31mComando inválido')
    
elif computador==2:#Computador jogou TESOURA
    if jogador==0:
        print('JOGADOR VENCEU')
    elif jogador==1:
        print('COMPUTADOR VENCEU')
    elif jogador==2:
        print('EMPATE')
    else:
        print('\033[1;31mComando inválido')