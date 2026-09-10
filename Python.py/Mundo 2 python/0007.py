r1=float(input('Primeiro segmento:'))
r2=float(input('Segundo segmento:'))
r3=float(input('Terceiro segmento:'))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os valores acima \033[1;32mPODEM\033[m formar um triângulo.',end='')
    if r1==r2==r3:
        print('EQUILÁTERO.') 
    elif r1!=r2!=r3!=r2: 
        print('ESCALENO')  
    else:
        print('ISÓCELES')
else:
    print('Os valores acima \033[1;31mNÃO\033[m podem formar um triângulo')
    exit()
if r1==r2==r3:
    print('O triângulo é equilátero.')