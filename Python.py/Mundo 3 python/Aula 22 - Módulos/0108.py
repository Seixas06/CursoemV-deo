from utilidadescev.moeda import metade, dobro, aumento, moeda, diminuir

num=float(input('Digite o preço: R$'))
print(f'A metade de {moeda(num)} é {moeda(metade(num))}')
print(f'O dobro de {moeda(num)} é {moeda(dobro(num))}')
print(f'Aumentando 10%, temos {moeda(aumento(num,10))}')
