while True:
    v=float(input('Valor disponível:'))
    if v >= 0 and v <= 2000:
        break 
while True:
    a=float(input('Açougue:'))
    if a >= 1 and a <= 1000:
        break
while True:
    f=float(input('Farmácia:'))
    if f >= 1 and f<=1000:
        break
while True:
    p=float(input('Padaria:'))
    if p >= 1 and p <= 1000:
        break
t=0

if v>=a:
    v-=a
    t+=1
if v>=f:
    v-=f
    t+=1
if v>=p:
    v-=p
    t+=1
    

print(f'Vô João consegue pagar {t} contas')
