from utilidadescev.moeda import resumo


def leiaDinheiro(msg):
    inpr=0
    while True:
        pr=str(input(msg)).replace(',','.')
        if pr.isalpha() or pr.strip()=='':
            print(f'\033[31mERRO: "{pr}" é um preço inválido!\033[m')
        elif pr.isdigit() or '.' in pr:
            pr=float(pr)
            break
    return pr
