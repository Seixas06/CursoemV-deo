from random import randint
from time import sleep


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(0,5):
        n=randint(1,10)
        numeros.append(n)
        print(f'{n}',end=' ',flush=True)
        sleep(0.3)
    sleep(0.5)
    print('PRONTO!')
    
    
def somapar():
    soma=0
    for i,v in enumerate(numeros):
        if v%2==0:
            soma+=v
    print(f'Somando todos os valores de {numeros}, temos {soma}')


numeros=list()
sorteia()
somapar()
