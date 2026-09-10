#Importa as bibliotecas
from random import randint
from time import sleep

#Numera variáveis
contagem=0
vida=5

#Randomiza computador
computador=randint(1,100)

#Apresenta o jogo
print('Vou pensar em um número inteiro entre 1 e 100. Tente adivinhar!')
print('VOCÊ TEM 6 TENTATIVAS')
print('Pensando...')
sleep(1)

#Pergunta o número ao jogador
n=int(input('Em que número pensei? '))

#Laço de tantativas erradas
while n<1 or n>100:
    n=int(input('Inválido. Tente novamente: '))
print('{} tentativas restantes'.format(vida)) 
    
#Laço de possibilidades com tentativas aceitas
while computador!=n:
    
    #Se o número for menor que o computador
    if n<computador:
        n=int(input('Mais... Tente outra vez: '))
        contagem+=1
        vida-=1
        print('{} tentativas restantes'.format(vida)) 
        
        #Se a respota for inválida
        while n<1 or n>100 or n//2==1:  
            n=int(input('Inválido. Tente novamente:'))
            if n>1 and n<100:
                vida-=1
                contagem+=1
                print('{} tentativas restantes'.format(vida)) 
    
    #Se o número for maior que o computador
    if n>computador:
        n=int(input('Menor... Tente outra vez: '))
        contagem+=1
        vida-=1
        print('{} tentativas restantes'.format(vida)) 
        
        #Se a respota for inválida
        while n<1 or n>100: 
            n(int(input('Inválido. Tente novamente:')))
    
    #Mensagem se o jogador acertar
    if n==computador and vida!=0:
        print('Você acertou! O número escolhido era {}'.format(n))
    
    #Mensagem se o jogador errar
    if vida==0 and n!=computador:
        print('Você perdeu! HAHAHAH!!! O número escolhido era {}'.format(computador))
        exit()   
print('Você acertou em {} tentativas.'.format(contagem+1))
