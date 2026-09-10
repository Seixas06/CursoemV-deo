from utilidadescev.moeda import metade, dobro, aumento

num=float(input('Digite o preço: R$'))
print(f'A metade de R${num:.2f} é R${metade(num):.2f}')
print(f'O dobro de R${num:.2f} é R${dobro(num):.2f}')
print(f'Aumentando 10%, temos R${aumento(num,10):.2f}')
