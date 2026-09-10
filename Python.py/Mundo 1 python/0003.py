print('Vamos calcular a média entre seus dois alunos?')
a1=float(input('Digite a nota do primeiro aluno: '))
n1=(input('Qual o nome do primeiro aluno? '))
print('A nota de {} é {}'.format(n1,a1))
a2=float(input('Digite a nota do segundo aluno: '))
n2=(input('Digite o nome do segundo aluno:'))
print('A nota de {} é {}'.format(n2,a2))
m=(a1+a2)/2
print('A média das notas entre {} e {} é {:.1f}'.format(n1,n2,m))