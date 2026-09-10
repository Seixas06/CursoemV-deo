from def115 import titulo
from arquivo115 import *
from time import sleep

c=('\033[30m', #cinza  0
    '\033[31m', #vermelho 1
    '\033[32m', #verde    2
    '\033[33m', #amarelo  3
    '\033[34m', #azul     4
    '\033[35m', #roxo     5
    '\033[36m', #ciano    6
    '\033[37m', #branco    7
    );

arq='cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    sleep(3)
    tam=titulo('MENU PRINCIPAL')
    print(f'''
    {c[3]}1{c[7]} - {c[4]}Ver pessoas cadastradas
    {c[3]}2{c[7]} - {c[4]}Cadastrar nova pessoa
    {c[3]}3{c[7]} - {c[4]}Sair do sistema{c[7]}
    ''')
    print('-'*tam)
    while True:
        try:
            opc=int(input(f'{c[2]}Sua opção: {c[7]}'))
            if opc<1 or opc>3:
                print(c[1],'ERRO: por favor digite uma opção válida!',c[7])
                continue
        except (ValueError):
            print(c[1],'ERRO: por favor digite um número inteiro válido!',c[7])
        else:
            break
    print('-'*tam)
    if opc==1:
        #Opção de listar o conteúdo do arquivo!
        lerArquivo(arq)
    elif opc==2:
        titulo('NOVO CADASTRO')
        nome=input('Nome: ')
        while True:
            try:
                idade=int(input('idade: '))
            except:
                print(c[1],'Digite uma idade válida',c[7])
            else:
                break
        cadastrar(arq,nome,idade)
    else:
        print('Até logo! Encerrando...')
        print('-'*tam)
        break
