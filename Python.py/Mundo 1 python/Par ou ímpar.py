print('\033[1;32;32m-=-\033[m'*5)
print('\033[1;35;35m PAR OU ÌMPAR?\033[m')#Título
print('\033[1;32;32m-=-\033[m'*5)
num=int(input('\033[1;33;33mDigite um número inteiro para saber se é par ou ímpar: \033[m'))#Pede para digitar o número
resultado=num%2#Calcula para saber se é par ou ímpar
if resultado==0:
    print('\033[1;34;34mPAR\033[m')#Resultado par
else:
    print('\033[1;31;31mÍMPAR\033[m')#Resultado ímpar1