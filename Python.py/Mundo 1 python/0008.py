print('Digite a seguir o valor a ser calculado o desconto e o número do deconto\n Ex:Se o produto terá 5% de desconto, digite 5! ')
product=float(input('Digite o valor do produto R$'))
desc=int(input('Digite o desconto: %'))
vad=product*desc
vd=vad/100
vf=product-vd
print('valor após o desconto será de R${:.2f}'.format(vf))