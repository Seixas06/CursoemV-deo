from math import factorial 
n=int(input('Digite um número para\ncalcular seu Fatorial: '))
c=n
fator=factorial(n)
print('Calculando {}! ='.format(n), end=' ')
while c>0:
    if c>1:
        print('{} X'.format(c), end=' ')
        c-=1
    else:
        print('{}'.format(c), end=' ')
        c-=1
    if c==0:
        print('= {}'.format(fator))
