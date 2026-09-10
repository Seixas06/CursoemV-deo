soma=0
maiorh=0
nomevelhoh=0
menor20=0
for pessoa in range(1,5):
    print('-'*5,'{}ª PESSOA'.format(pessoa),'-'*5)#Apresenta 'x PESSOA'
    nome=(input('NOME: ')).strip().title()#Pergunta o nome
    idade=int(input('IDADE: '))#Pergunta idade
    sexo=(input('SEXO [M/F]: ')).strip().upper()#Pergunta o sexo
    if sexo=='M' or sexo=='MASCULINO':
        if pessoa==1:
            maiorh=idade
            nomevelhoh=nome
        else:
            if idade>maiorh:
                maiorh=idade
                nomevelhoh=nome
        if sexo in 'FFEMININO' and idade<20:
            menor20+=1
    soma+=idade
    media=soma/pessoa
#Apresenta os dados recolhidos
print('A média de idade do grupo é de {:.0f} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorh,nomevelhoh))
print('Ao todo são {} mulheres com menos de 20 anos'.format(menor20))