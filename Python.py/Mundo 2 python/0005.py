from time import sleep
#Apresenta o programa
print('Digite as notas para calcular a média e descobrir aprovação.')

#Pergunta a nota dos alunos
n1=float(input('Digite a 1º nota: '))
n2=float(input('Digite a 2º nota: '))

#Calcula média e apresenta
media=(n1+n2)/2
print('A média entre {;.1f} e {:.1f} é {:.1f}'.format(n1,n2,media))
#determina possibilidades
if media<5:
    print('Você foi \033[1;31mREPROVADO\033[m')
elif media>=5 and media<6.9:
    print('Você está de \033[1;33mRECUPERAÇÃO\033[m')
elif media>=7:
    print('Você foi \033[1;32mAPROVADO\033[m')
    