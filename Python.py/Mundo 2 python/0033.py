from random import randint 
cont=0
print('=-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*30)
while True:
    computador=randint(1,10)
    jogador=int(input('Digite um valor de 1 a 10: '))
    tipo=' '
    while tipo not in 'PIÍ':
        tipo=str(input('Par ou ímpar? [P/I]: ')).upper().strip()[0]
    soma=jogador+computador
    print('-'*26)
    if soma%2==0:
        par=soma
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}, PAR')
    else:
        impar=soma
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}, ÍMPAR')
    print('-'*26)
    if tipo=='P' and soma%2==0:
        print('Você VENCEU!\nVamos jogar novamente...')
        cont+=1
    elif tipo in 'IÍ' and soma%2!=0:
        print('Você VENCEU!\nVamos jogar novamente...')
        cont+=1
    else:
        print('Você perdeu!\n','=-'*13,f'\nGAME OVER! Você venceu {cont} vezes')
        break