cont=0
while True:
    n=int(input('Quer ver a tabuada de qual valor? '))
    cont+=n
    print('-'*30)
    for t in range(1,11):
        result=n*t
        print(f'{n} X {t} = {result}')
    print('-'*30)
    if n<=0:
        break
print('PROGRAMA DE TABUADA ENCERRADO, VOLTE SEMPRE!')