from math import hypot
c1=float(input('Digite o cateto oposto:'))
c2=float(input('Digite o cateto adjacente:'))
hipo=hypot(c1,c2)
print('A hipotenusa vale {:.2f}'.format(hipo))