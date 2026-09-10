jogador={}
time=[]
partidas=[]
while True:
    jogador.clear()
    jogador['nome']=input('Nome do jogador: ').title()
    tot=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for p in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {p+1}? ')))
    jogador['gols']=(partidas[:])
    jogador['total']=sum(partidas)
    time.append(jogador.copy())
    while True:
        continuar=str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! RESPONDA SOMENTE S OU N.')
    if continuar in 'N':
        break
print('=-'*30)
print('cod',end=' ')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'*60)
for k,v in enumerate(time):
    print(f'{k:>3}',end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*60)
while True:
    busca=int(input('Mostrar dados de qual jogador? "999" para parar. '))
    if busca>=len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {time[busca]["nome"].upper()}')
        for i,g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*60)
    if busca==999:
        break
print('<<<Volte Sempre!>>>')
