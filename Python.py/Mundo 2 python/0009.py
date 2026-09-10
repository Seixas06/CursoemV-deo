#Pergunta o valor da compra, apresenta opções e pergunta qual é
compra=float(input('Digite o valor da compra: '))
print('Escolha uma forma de pagamento.\n[1] À vista no dinheiro.\n[2] À vista no cartão.\n[3] Em até 2x no cartão.\n[4] 3x ou mais no cartão.')
opc=str(input('Qual é a opção?')).strip()
#Dá as possibilidades de acordo com a escolha
if opc=='3' or opc=='4':
    #Se for parcelado pergunta o número de parcelas
    parcelas=int(input('Quantas parcelas?'))
    if parcelas<=2:
        print('O valor final da compra sem acréscimo ou desconto será de {:.2f}'.format(compra))
    else:
        juros=(compra*20/100)+compra
        parcela=juros/parcelas
        print('Parcelando 3x ou mais no cartão, você fica com 20% de juros.\nSua compra parcelada em {} vezes de {:.2f} COM JUROS\nSua compra de {:.2f} custará R${:.2f}'.format(parcelas,parcela,compra,juros))
elif opc=='1':
    desconto=compra-compra*10/100
    print('Pagando à vista você ganha 10% de desconto.\nO valor final é R${:.2f}'.format(desconto))
elif opc=='2':
    desconto=compra-compra*5/100
    print('Pando à vista no cartão você ganha 5% de desconto\nO valor final é R${:.2f}'.format(desconto))
else:
    print('\033[1;31mOpção inválida.\nTente novamente.')