from time import sleep
aluno=list()
turma=list()
while True:
    aluno.append(str(input('Nome: ')))
    aluno[0].title()
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    turma.append(aluno[:])
    aluno.clear()
    continuar=str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar=='N':
        break
print('=-'*40)
print(f'{"N1º.":<4} {"NOME":<10} {"MÉDIA":>8}')
print('-'*80)
for n,i in enumerate (turma):
    media=(i[1]+i[2])/2
    print(f'{n:<4}{i[0].title().strip():<10}{media:8.1f}')
while True:
    nota=int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if nota==999:
        break
    if nota <= len(turma)-1:
        print(f'As notas de {turma[nota][0]} são {turma[nota][1],turma[nota][2]} ')
print('FINALIZANDO...')
sleep(2)
print('<<<VOLTE SEMPRE>>>')