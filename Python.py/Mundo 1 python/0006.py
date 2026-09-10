print('Digite um valor em reais para calcular quantos dólares você pode adquirir')
rc=float(input('Quantos reais você tem a disposição? R$'))
d=rc/5.76
print('Com R${:.2f} você pode comprar US${:.2f}'.format(rc,d))