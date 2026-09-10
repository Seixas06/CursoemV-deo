#Pergunta os números
n1=float(input('Primeiro número: '))
n2=float(input('Segundo número: '))
opc=0

#Repete a estrutura de escolha
while opc!=5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opc=int(input('>>>>> Qual sua opção? '))
    while opc<1 or opc>5:
        opc=int(input('Inválido. Tente novamente: '))
    
    #Soma os escolhidos
    if opc==1:
        r=n1+n2
        print('A soma entre {} e {} resulta em {}'.format(n1,n2,r))
    
    #Multiplica os escolhidos
    if opc==2:
        r=n1*n2
        print('A multiplicção entre {} e {} resulta em {}.'.format(n1,n1,r))

    #Verifica maior ou igualdade
    if opc==3:
        if n1>n2:
            maior=n1
        elif n1<n2:
            maior=n2
        if n1>n2 or n2>n1:
            print('O maior número entre {} e {} é {}'.format(n1,n2,maior))
        elif n1==n2:
            print('Os números são iguais.')
    
    #Pergunta novos números
    if opc==4:
        print('Informe novamente os números')
        n1=float(input('Primeiro número:'))
        n2=float(input('Segundo número: '))
        
    #Fecha o programa
    print('=-'*15)
if opc==5:
    print('Finalizando...')
