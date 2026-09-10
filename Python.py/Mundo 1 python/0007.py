print('Para calcular a quantidade de tinta para pintar uma superfície,\n digite os valores a seguir')
l=float(input('Largura:'))
a=float(input('Altura:'))
area=l*a
t=area/2
print('Para pintar uma parede com {:.2f}m², será necessário {:.2f} litros de tinta'.format(area,t))