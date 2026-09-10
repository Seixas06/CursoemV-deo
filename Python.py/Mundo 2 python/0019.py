from datetime import date
atual=date.today().year
menores=0
maiores=0
for c in range(1,8):
    nasc=int(input('Qual a {}ª data de nascimento?'.format(c)))
    idade=atual-nasc
    if idade<18:
        menores+=1
    else:
        maiores+=1
print('{} são menores de idade'.format(menores))
print('{} são maiores de idade'.format(maiores))