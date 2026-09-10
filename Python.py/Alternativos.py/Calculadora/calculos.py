
def calcular(expre):
    permitido='0123456789+-*/.'
    for c in expre:
        if c not in permitido:
            return 'Inválido'
    try:
        return str(eval(expre))
    except ZeroDivisionError:
        return 'Divisão por 0'
    except:
        return 'Erro'