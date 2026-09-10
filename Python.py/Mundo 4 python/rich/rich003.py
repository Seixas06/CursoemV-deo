from rich import print
from rich.table import Table

tabela=Table(title='Tabela de preços')
tabela.add_column('NOME',justify='left',style='yellow')
tabela.add_column('PREÇO',justify='center',style='green')
tabela.add_row('Lápis','R$2,00')


print(tabela)