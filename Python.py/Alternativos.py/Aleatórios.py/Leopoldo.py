from tkinter import * 
from PIL import Image, ImageTk

def starter():
    gatoganha = Label(calculadora, image=gatosentado)
    gatoganha.place(x=600, y=200)
    start.destroy()

    vini = Label(calculadora, image=vinioc)
    vini.place(x=10, y=200)

calculadora = Tk()
calculadora.title('Éguas')
calculadora.geometry('1200x800+600+120')
calculadora.config(bg='white')
calculadora.iconbitmap('favicon (1).ico')

titulo = Label(
    calculadora,
    text='Quem são os mais Éguas do Vôvis?',
    font=('Vogue', 40),
    bg='Blue',
    fg='Yellow',
    relief='groove',
    borderwidth=10,
    anchor='center'
)
titulo.place(x=162, y=70)

vini_img = Image.open('Vinioc.jpeg').resize((300, 300))
vinioc = ImageTk.PhotoImage(vini_img)

gato_img = Image.open('LeogatoSentado.jpeg').resize((300, 300))
gatosentado = ImageTk.PhotoImage(gato_img)

start = Button(
    calculadora,
    text='Descubra os maiores comedores de maçã', 
    font=('Vogue', 25),
    bg='Blue',
    fg='White',
    command=starter
)
start.place(x=100, y=200)

calculadora.mainloop()
