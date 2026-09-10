total=maiormil=menor=cont=0
barato=''
while True:
    nome=(input('Produto comprado:')).strip().title()
    preço=float(input('Preço: R$'))
    cont+=1
    total+=preço
    print('-'*30)
    resposta=' '
    while resposta not in 'SN':
        resposta=(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if preço>1000:
        maiormil+=1
    if cont==1 or preço<menor:
        menor=preço
        barato=nome
    if resposta=='N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maiormil} custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor}')