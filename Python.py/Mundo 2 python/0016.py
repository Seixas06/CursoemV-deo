print('10 termos de uma PA')
primeiro=int(input('Primeiro termo:'))
razao=int(input('Razão: '))
decimo=primeiro+(10-1)*razao
for c in range(primeiro,decimo,razao):
    print(c,end=' > ')
print('Acabou')