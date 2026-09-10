nome=str(input('Qual é seu nome? ')).strip().title()
if nome=='Mateus' or nome=='Teteu':
    print('Que nome lindo você tem!'.format(nome))
elif nome=='Seixas':
    print('Realmente um belo nome! {}'.format(nome))
elif nome in 'Manu Manuela Ana Beatriz':
    print('Você é irmã do Mateus, {}?'.format(nome))
elif nome in 'Lucas Leo Leonardo':
    print('Você é irmão do Mateus, {}?'.format(nome))
elif nome=='Leandro':
    print('Olá pai do Mateus')
elif nome=='Gildeanne' or nome=='Gil':
    print('Olá mãe do Mateus')
elif nome in 'Tayssa Taynara Aline Luiza Lulu Raquel':
    print('Você é da família do Mateus, {}'.format(nome))
else:
    print('Que nome normal.')
print('Tenha um bom dia, {}!'.format(nome))