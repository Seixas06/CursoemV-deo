import time 
print('\033[1;33;33mBEM VINDO AO RADAR ELETRÔNICO!\033[m')
time.sleep(1)
velocidade=float(input('\033[4;34;34mQual a velocidade do carro em Km/h? \033[m'))#Pergunta a velocidade
if velocidade >80:
    print('\033[1;31;31mVocê precisa ser mais consciente!\nMultado pelo excesso de velocidade, a multa custará R${:.2f}\033[m'.format(velocidade,(velocidade-80)*7))#Velocidade acimad de 80
else:
    print('\033[1;32;32mParabéns! Você está dentro do limite de velocidade\033[m')#Velocidade abaixo de 80
