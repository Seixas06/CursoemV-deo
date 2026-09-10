print('Descubra o valor a pagar pelo aluguel do carro')
dias=int(input('Quantos dias você ficou com o carrro? '))
km=float(input('Quantos km rodados? '))
valoraluguel=dias*60+km*0.15
print('O aluguel por {} dias com {:.2f} custará R${:.2f}'.format(dias,km,valoraluguel))