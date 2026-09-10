pergunta=(input('Qual o sexo? [M/F]:')).strip().upper()[0]
while pergunta not in 'MF':
        pergunta=(input('\033[1;31mDados inválidos.\033[m Por favor, informe o sexo [M/F]:')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(pergunta))