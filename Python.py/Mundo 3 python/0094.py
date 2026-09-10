pessoa=dict()
dados=list()
mulheres=list()
soma=media=0
while True:
    pessoa['nome']=input('Nome: ').title().strip()
    while True:
        pessoa['sexo']=(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! Responda apenas M ou F.')
    if pessoa['sexo'] in 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade']=int(input('Idade: '))
    dados.append(pessoa.copy())
    soma+=pessoa['idade']
    media=soma/len(dados)
    while True:
        continuar=str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'N' or continuar in'S':
            break
        else:
            print('ERRO! Responda apenas com S ou N.')
    if continuar=='N':
        break
print('=-'*30)
print(f'''A) Ao todo tem {len(dados)} pessoas cadrastadas.
B) A média de idade é {media:.1f} anos.''')
if len(mulheres)==1:
    print('C) A mulher cadastrada foi ',end=' ')
    for n,i in enumerate(mulheres):
        print(i)
elif len(mulheres)>1:
    print('C) As mulheres cadastradas foram', end=' ')
    for n,i in enumerate(mulheres):
        print(i,end=' ')
elif len(mulheres)==0:
    print('C) Não há mulheres cadastradas.')
print(f'\nLista de pessoas que estão acima da média:')
for p in dados:
    if p['idade']>media:
        print('     ',end='')
        for k,v in p.items():
            print(f'{k} = {v}',end=' ')
        print()
print('<<<ENCERRADO>>>')
