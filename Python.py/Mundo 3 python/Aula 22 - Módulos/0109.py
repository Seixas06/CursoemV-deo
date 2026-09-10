from utilidadescev.moeda import metade, dobro, aumento, moeda, diminuir

num=float(input('Digite o preço: R$'))
print(f'A metade de {moeda(num)} é {metade(num,True)}')
print(f'O dobro de {moeda(num)} é {dobro(num,True)}')
print(f'Aumentando 10%, temos {aumento(num,10,True)}')
print(f'Reduzindo 13%, temos {diminuir(num,13,True)}')
