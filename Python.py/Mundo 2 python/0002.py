num=int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para conversão.
[1] Para BINÁRIO
[2] Para OCTAL
[3] Para HEXADECIMAL''')
escolha=int(input('Sua escolha:'))
if escolha==1:
    print('A conversão de {} para BINÁRIO é {}'.format(num,bin(num)[2:]))
elif escolha==2:
    print('A conversão de {} para OCTAL é {}'.format(num,oct(num)[2:]))
elif escolha==3:
    print('A conversão de {} para HEXADECIMAL é {}'.format(num,hex(num)[2:]))
else:
    print('\033[1;31mOpção inválida. Tente novamente.\033[m')