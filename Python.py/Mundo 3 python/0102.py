def fatorial(num,show=False):
    '''
    -> Calcula fatorial de um número
    :param n: número a ser calculado fatorial.
    :param show: Determina se o cálculo aparece usando True ou False
    :retur f: O fatorial de n
    '''
    c=num
    f=1
    for n in range (num,0,-1):
        if show:
            print(n, end=' ')
            if n>1:
                print(' x ', end=' ')
            else:
                print(' = ',end=' ')
        f*=n
    return f 


print(fatorial(5,show=True))
help(fatorial)
