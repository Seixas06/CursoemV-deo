from time import sleep
from random import randint
from operator import itemgetter
jogo={'jogador 1': randint(1,6),
      'jogador 2': randint(1,6),
      'jogador 3': randint(1,6),
      'jogador 4': randint(1,6)}
ranking=[]
print('Valores sorteados:')
for k,v in jogo.items():
    print(f'O {k} tirou o número {v} no dado.')
    sleep(1)
sleep(1.5)
print('=-'*30)
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('   == RANKING DOS JOGADORES ==')
for i,v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)