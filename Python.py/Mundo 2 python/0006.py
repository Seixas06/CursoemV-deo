from datetime import date
#Pergunta ano de nascimento do atleta
nasc=int(input('Qual o ano de nascimento do atleta? '))

#Calcula idade do atleta
atual=date.today().year
idade=atual-nasc
print('O atleta tem {} anos'.format(idade))

#Define as possibilidades de acordo com a idade do atleta
if nasc<=9:
    print('A categoria do atleta é MIRIM.')
elif 9<nasc<=14:
    print('A categoria do atleta é INFANTIL')
elif 14<nasc<=19:
    print('A categoria do atleta é JUNIOR')
elif 19<nasc<=25:
    print('A categoria do atleta é SÊNIOR')
else:
    print('A categoria do atleta é MASTER')