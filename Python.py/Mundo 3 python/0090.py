aluno=dict()
aluno['nome']=str(input('Nome: ')).title()
aluno['media']=float(input(f'Média de {aluno["nome"]}: '))
print('=-'*30)
if aluno['media']<5:
    aluno['situação']='reprovado'
elif aluno['media']<7:
    aluno['situação']='recuperação'
else:
    aluno['situação']='aprovado'
for k,v in aluno.items():
    print(f'- {k} é igual a {v}')