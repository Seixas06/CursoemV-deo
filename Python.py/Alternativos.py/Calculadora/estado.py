from tkinter import END
from calculos import calcular

valores=[]

def atualizar_display(entrada):
    entrada.delete(0,END)
    entrada.insert(END,''.join(valores))
    
    
def adicionar(v,entrada):
    valores.append(str(v))
    atualizar_display(entrada)
    
    
def apagar(entrada):
    if valores:
        valores.pop()
        atualizar_display(entrada)


def limpar(entrada):
    valores.clear()
    atualizar_display(entrada)
    
    
def resultado(entrada):
    expr=''.join(valores)
    res=calcular(expr)
    valores.clear()
    valores.append(str(res))
    # valores.append('Alguém já calculou isso!')
    atualizar_display(entrada)
    
