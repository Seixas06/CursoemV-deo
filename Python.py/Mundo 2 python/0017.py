n=int(input('Digite um número:'))
tot=0
for c in range(1,n+1):
    if n%c==0:
        print('\033[33m',end='')
        tot+=1
    else:
        print('\033[31m',end='')
    print(c,end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(n,tot))
if tot>2:
    print('Ele NÃO É PRIMO')
elif tot==2:
    print('Ele é PRIMO')
else:
    print('Ele NÃO É PRIMO')