nome=str(input('Qual é o seu primeiro nome? ')).strip().title()
if nome=='Mateus':
    print('Que nome lindo você tem!!')
else:
    print('Seu nome é tão normal')
print('Olá {}, prazer em te conhecer.'.format(nome))