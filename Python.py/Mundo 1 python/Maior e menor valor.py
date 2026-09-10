n1=float(input('Digite o número 1:'))
n2=float(input('Digite o número 2:'))
n3=float(input('Digite o número 3:'))
#Verificando quem é menor
menor=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
#Verificando quem é maior
maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print('O menor valor é {}\n O maior valor é {}'.format(menor,maior))
