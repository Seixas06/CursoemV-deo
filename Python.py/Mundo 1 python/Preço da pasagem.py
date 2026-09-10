dist=float(input('\033[1;35;35mQual a distância da viagem em km?\033[m'))#Pergunta a distância
if dist>200:
    print('\033[1;34;34mA cima de 200km, é dado um desconto.\n passagem custará apenas R${:.2f}\033[m'.format(dist*0.45))#Calcula a passagem maior de 200km
else:
    print('\033[1;32;32mA passagem custará R${:.2f}\033[m'.format(dist*0.5))#Calcula passagem menor de 200km