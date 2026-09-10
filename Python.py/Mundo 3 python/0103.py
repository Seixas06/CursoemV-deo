def ficha(nom='<desconhecido>',gol=0):
    print(f'O jogador {nom} fez {gol} gol(s) no campeonato')


print('-'*30)
nome=str(input('Nome do jogador: '))
gols=str(input('Número de gols: '))
if gols.isnumeric():
    gols=int(gols)
else:
    gols=0
if nome.strip()=='':
    ficha(gol=gols)
else:
    ficha(nome,gols)
