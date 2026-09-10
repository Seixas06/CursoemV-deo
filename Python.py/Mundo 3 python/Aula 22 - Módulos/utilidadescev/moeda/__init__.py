def metade(n=0, format=False):
    met=n/2
    return met if format is False else moeda(met) 


def dobro(n=0,format=False):
    dob=n*2
    return dob if format is False else moeda(dob)


def aumento(n=0,t=0,format=False):
    aum=n+(n*t/100)
    return aum if not format else moeda(aum)


def diminuir(n=0,t=0,format=False):
    dim=n-(n*t/100)
    return dim if not format else moeda(dim)


def moeda(n=0,m='R$'):
    return f'{m}{n:.2f}'.replace('.',',')


def resumo(n=0,au=0,re=0):
    msg='RESUMO DO VALOR'
    tam=len(msg)+24
    print('-'*tam)
    print(f'            {msg}')
    print('-'*tam)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço:  \t{dobro(n,True)}')
    print(f'Metade do preço: \t{metade(n,True)}')
    print(f'{au}% de aumento:  \t{aumento(n,au,True)}')
    print(f'{re}% de redução:  \t{diminuir(n,re,True)}')
    print('-'*tam)
