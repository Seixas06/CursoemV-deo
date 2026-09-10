soma=0
cont=0
for c in range(1,7):
    valor=int(input('Digite o {}º valor inteiro:'.format(c)))
    if valor%2==0:
        cont+=1
        soma+=valor
print('Você informou {} números pares e a soma deles foi {}'.format(cont,soma))