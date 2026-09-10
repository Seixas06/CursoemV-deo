def area(l,c):
    
    
    a=l*c
    print(f'A área de um terreno {largura:.1f}X{comprimento:.1f} é de {a}')
print('Controle de Terrenos')
print('-'*30)
largura=float(input('LARGURA (m): '))
comprimento=float(input('COMPRIMENTO (m): '))
area(largura,comprimento)