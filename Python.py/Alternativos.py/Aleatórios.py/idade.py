maior=menor=meio=0
while True:
    n1=int(input())
    n2=int(input())
    n3=int(input())
    if 5<=n1<=100 and 5<=n2<=100 and 5<=n3<=100:
        break
if n3<=n1<=n2:
    meio=n1
elif n2<=n1<=n3:
    meio=n1
else:
    if n1<=n2<=n3:
        meio=n2
    elif n3<=n2<=n1:
        meio=n2
    else:
        if n1<=n3<=n2:
            meio=n3
        elif n2<=n3<=n1:
            meio=n3
        
    
print(f'{meio}')