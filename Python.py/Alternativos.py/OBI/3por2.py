c=n=soma=0
pr=gp=[]
while True:
    n=int(input('N: '))
    if 1<=n<=100000:
        break
while c<n:
    while True:
        p=int(input(f'P{c+1}:'))
        if 1<=p<=1000:
            pr.append(p)
            c+=1    
            break
for c in range(0,3):
    gp.append(max(pr))
    pr.remove(max(pr))
for i in range(0,2):
    soma += max(gp)
print(soma)