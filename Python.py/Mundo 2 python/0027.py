#Apresenta e pergunta os termos
print('Gerador de PA\n','-='*10)
primeiro=int(input('Primeiro termo: '))
razao=int(input('Razão da PA: '))

#Calcula PA
mais=0
termo=primeiro
contador=1
total=0
mais=10
while mais!=0:
    total+=mais
    while contador<=total:
        print('{} >'.format(termo),end=' ')
        termo+=razao
        contador+=1
    print('PAUSA')

    #Pergunta quantos termos o usuário deseja mostrar mais
    mais=int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print('Progressão finalizada com {} termos'.format(total))