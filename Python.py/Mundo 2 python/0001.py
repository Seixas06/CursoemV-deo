valor=float(input('Qual o valor da casa em R$? R$'))
salario=float(input('Qual o salario do comprador? R$'))
anos=int(input('Em quantos anos ele vai pagar?'))
prestação=valor/(anos*12)
minimo=salario*30/100
print('\033[1;34mPara pegar uma casa de {:.2f} em {} anos, a prestação será de {:.2f}\033[m'.format(valor,anos,prestação))
if prestação<=minimo :
    print('\033[1;32mCONCEDIDO\033[m')
else:
    print('\033[1;31mNegado\033[m')
