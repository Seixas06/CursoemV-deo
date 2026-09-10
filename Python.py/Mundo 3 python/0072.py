cont=('zero', 'um', 'dois','três','quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
     'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
     'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n=int(input('Digite um número inteiro entre 0 e 20: '))
        if -1<n<21:
            break
        print('Tente novamente.', end=' ')
    print(f'Você digitou o número {cont[n]}')
    while True:
        resp=(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
        if resp == 'S' or resp == 'N':
            break
    if resp=='N':
        break