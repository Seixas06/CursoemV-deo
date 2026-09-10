r1=float(input('Digite o valor da primeira reta: '))
r2=float(input('Digite o valor da terceira reta: '))
r3=float(input('E por fim digite o valor da terceira reta: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os números escolhidos podem formar um triângulo')
else:
    print('Os números escolhidos não podem formar um triângulo')