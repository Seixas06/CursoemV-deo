from time import sleep


def contador(i,f,q):
    if q==0:
        q=1
    elif q<0:
        q*=-1
    print('-'*30)
    print(f'Contagem de {i} até {f} de {q} em {q}\n')
    if i<f:
        for n in range(i,f+1,q):
            print(n,end=' ',flush=True)
            sleep(0.3)
    if i>f:
        for n in range(i,f-1,-q):
            print(n,end=' ',flush=True)
            sleep(0.3)
    print('FIM!')


#Programa principal
contador(1,10,1)
contador(10,0,2)
print('-'*30)
print('Sua vez!')
i=int(input('Digite o inicio da sua contagem: '))
f=int(input('Defina o fim da sua contagem: '))
q=int(input('Defina o passo da sua contagem:'))
contador(i,f,q)
print('-'*30)
