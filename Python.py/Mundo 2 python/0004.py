from datetime import date
from time import sleep
import sys
atual=date.today().year

#Apresentação
print('\033[1;34mBem vindo!\nInforme seu gênero e ano de nascimento para continuar.\033[m ')
sleep(0.5)

#Verifica mulheres e retira do operação
while True:
    sexo=str(input('\033[1;33mQual seu gênero?\033[m ')).strip().upper()[:3]
    if sexo== 'FEM' or sexo== 'MUL':
        print('\033[1;32mVocê não precisa de alistamento obrigatòrio.\033[m')
        while True:
            
            #Pergunta se as mulheres ainda querem participar
            sn=str(input('Você ainda quer verificar? Digite \033[1;32mSIM\033[m ou \033[1;31mNÃO\033[m: ')).strip().upper()[:2]
            if sn=='NÃ':
                sys.exit()
            if sn=='SI': 
                 break
            if sn!='SI' or sn!='NÃ':
                print('\033[1;31mTente novamente.\033[m')
                sys.exit()
            
            #Mulheres que aceitaram se juntam ao homens
        break
    elif sexo=='MAS' or sexo=='HOM':
        break

#verifica idade para homens ou mulheres que aceitaram
nascimento=int(input('\033[1;33mQual o ano de nascimento?\033[m '))
idade=atual-nascimento
print('\033[1;36mQuem nasceu em {} tem ou fará {} anos em {}.\033[m'.format(nascimento,idade,atual))

#Verifica o alistamento para homens
if idade<18:
    print('\033[1;32mAinda não é hora de se alistar\nFaça isso daqui há {} anos, quando tiver 18'.format(18-idade))
    ano=atual+(18-idade)
    print('Seu alistamento será em {}\033[m'.format(ano))
elif idade>18:
    print('\033[1;31mVocê deveria ter se alistado há {} anos. Você já tem {}.\033[m'.format(idade-18,idade))
    ano=atual-(idade-18)
    print('\033[1;31mSeu alistamento deveria ter sido em {}\033[m'.format(ano))
elif nascimento!=int:
    print('\033[1;31mTente novamente.\033[m')
    exit()
else:
    print('\033[1;31mVocê está com 18 anos, aliste-se IMEDIATAMENTE.\033[m')
