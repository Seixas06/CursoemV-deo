from math import sin,cos,tan,radians
número=float(input('Digite o ângulo:'))
print('Seu ângulo é {}'.format(número))
print('O SENO é {:.2f} \n O COSSENO é {:.2f} \n A TANGENTE é {:.2f}'.format(sin(radians(número)),cos(radians(número)),tan(radians(número))))