maior=homens=mulheres=0
print('-'*30,'\n    CADASTRE UMA PESSOA')
print('-'*30)
while True:
    idade=int(input('Idade: '))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('-'*30)
    continuar=' '
    while continuar not in 'SN':
        continuar=str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    print('-'*30)
    
    #Verifica idade menor de 18
    if idade>18:
        maior+=1
    
    #Verifica se é homem ou mulher
    if sexo=='M':
        homens+=1
    if sexo=='F':
        if idade<20:
            mulheres+=1    
    if continuar=='N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')