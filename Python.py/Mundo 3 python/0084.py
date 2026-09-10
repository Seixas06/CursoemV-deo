dados=[]
pessoas=[]
mai=men=0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(pessoas)==0:
        mai=men=dados[1]
    else:
        if dados[1] > mai:
            mai=dados[1]
        if dados[1]<men:
            men=dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cont=input('Quer continuar? [S/N]: ').strip().upper()[0]
    if cont=='N':
        break
print('=-'*30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {mai}Kg. O peso de ',end='')
for p in pessoas:
    if p[1]==mai:
        print(p[0] )
print(f'O menor peso foi de {men}Kg. O peso de ',end='')
for p in pessoas:
    if p[1]==men:
        print(p[0])