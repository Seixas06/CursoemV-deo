def notas(*num,sit=False):
    """Notas da turma

    Args:
        sit: if True, adicionar ou não a situação do aluno. Defaults to False.
        n: Uma ou mais notas de alunos
    Returns:
        r: Retorna o dicionário da turma
    """
    r=dict()
    r['total']=len(num)
    r['maior']=max(num)
    r['menor']=min(num)
    r['média']=sum(num)/len(num)
    if sit:
        if r['média']>=7:
            r['situação']='BOA'
        elif r['média']>=5:
            r['situação']='RAZOÁVEL'
        else:
            r['situação']='RUIM'
    return r


resp=notas(10,8.5,2,4,sit=True)
print(resp)
help(notas)