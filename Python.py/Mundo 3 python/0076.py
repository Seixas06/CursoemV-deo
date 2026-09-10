listagem=('Lápis',1.75,'Borracha',1.50,'Estojo',10.90,
          'Mochila',49.90,'Caneta',2,'Caderno',15.90,
          'Régua',7.50,'Agenda',9.90,'Apontador',3.90)
print('-'*38)
print(f'{"LISTAGEM DE PREÇOS":^38}')
print('-'*38)
for item in range(0,len(listagem)):
    if item%2==0:
        print(f'{listagem[item]:.<30}',end='')
    else:
        print(f'R$ {listagem[item]:>5.2f}')
print('-'*38)