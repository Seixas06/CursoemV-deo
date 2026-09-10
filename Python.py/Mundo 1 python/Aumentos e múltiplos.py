salario=float(input('Qual é o salário do funcionário? '))
if salario>1250:
    print('O salário terá um aumento de 10%, ficando \033[1;32;23m{:.2f}\033[m'.format((salario*10/100)+salario))
else:
    print('O salário terá um aumento de 15%, ficando \033[1;32;32m{:.2f}'.format(salario*15/100+salario))