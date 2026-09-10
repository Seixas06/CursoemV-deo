print('Gerador de PA\n','-='*10)
primeiro=int(input('Primeiro termo: '))
razao=int(input('Razão da PA: '))
termo=primeiro
contador=1
while contador<=10:
    print('{}'.format(termo),end=' ')
    if contador<10:
        print('>',end=' ')
    elif contador>=10:  
        print('--',end=' ')    
    termo=termo+razao
    contador+=1
print('FIM')
