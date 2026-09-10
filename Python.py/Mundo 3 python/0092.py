from datetime import datetime
trabalhador=dict()
trabalhador['nome']=str(input('Nome: ')).strip().title()
trabalhador['idade']=int(input('Ano de nascimento: '))
trabalhador['ctps']=int(input('Carteira de Trabalho (0 não tem): '))
trabalhador['idade']=datetime.now().year-trabalhador['idade']
if trabalhador['ctps']!=0:
    trabalhador['contratação']=int(input('Ano de contratação: '))
    trabalhador['salario']=float(input('Salário: R$'))
    trabalhador['aposentadoria']=trabalhador['idade']+((trabalhador['contratação']+35)-datetime.now().year)
print('-='*30)
for k,v in trabalhador.items():
    print(f'- {k} tem o valor {v}')