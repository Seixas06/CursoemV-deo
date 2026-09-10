def leiaint(msg):
    while True:
        try:
            ni=int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mPor favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return ni


def leiafloat(msg):
    while True:
        try:
            nf=float(input(msg))
        except(ValueError,TypeError):
            print('\033[31mPor favor, digite um numero real válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return nf


ni=leiaint('Digite um número inteiro: ')
nf=leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {ni} e o real foi {nf}')
