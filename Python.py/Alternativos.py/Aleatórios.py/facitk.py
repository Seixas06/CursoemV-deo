from tkinter import *
from PIL import Image,ImageTk

def imagem(jan,img,l,h,rowm,col):
    """ Defina todos os parâmetros para criar a imagem

    Args:
        l,h (int): Largura e altura
        jan (str): janela em que vamos adiconar a imagem
        rowm,col (int): linha e coluna
        img (str): Imagem a ser colocada
    """
    trya= Image.open(img).resize((l,h))
    image1 = ImageTk.PhotoImage(trya)
    var = Label(jan, image=image1)
    var.grid(row=rowm,column=col)
    var.image= image1


#EXEMPLO
# imagem(janela,'LeogatoSentado.jpeg',300,300,1,2)
