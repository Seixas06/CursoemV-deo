resp='S'
contador=soma=0
while resp=='S':
    n=float(input('Digite um número: ')) 
    resp=str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    soma+=n
    contador+=1
    if contador==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
media=soma/contador
print('Você digitou {} números e a média foi {}'.format(contador,media))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))