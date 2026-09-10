n=int(input('Digite um número: '))
print('Você vai descobrir o dobro dele, o triplo e a raíz quadrada!!')
Resposta=str(input('Está preparado?'))
d=n*2
t=n*3
rq=n**(1/2)
print('O número {:=^20}, que você escolheu tem'.format(n), end=' >>> ')
print('{:.1f} como seu dobro, {:.1f} como seu triplo e {:.2f} como sua raíz quadrada!!'.format(d,t,rq))