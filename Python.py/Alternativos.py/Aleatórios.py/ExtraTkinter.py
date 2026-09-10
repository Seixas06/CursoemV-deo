from tkinter import * 
from time import sleep
from PIL import Image, ImageTk

#O que acontece ao apertar o botão "Start"
def starter():
    for widget in calculadora.winfo_children():
        widget.destroy()


#Parâmetros janela/criação
calculadora=Tk()
calculadora.title('Seixas Calculator')
calculadora.geometry('600x700+600+120')
calculadora.config(bg='darkblue')
calculadora.resizable(False,False)
calculadora.iconbitmap('favicon (5).ico')

#Coloca logo do Python na tela inicial
logo=Image.open('PyLogo (1).png').resize((300,300))
pylogo=ImageTk.PhotoImage(logo)
logopy=Label(calculadora,image=pylogo)
logopy.pack(pady=20)

#Titulo "Calculadora"
titulo=Label(
    calculadora, 
    text='Calculadora\ndo Seixas',
    font=('Vogue',40),
    bg='Blue',
    fg='Yellow',
    anchor='center',
    relief='groove',
    borderwidth=10,
    width=20
)
titulo.pack(pady=10,padx=30,ipady=5)

#Coloca o botão "Start"
start=Button(
    calculadora,
    text='Clique aqui para começar!', 
    font=('Vogue',25),
    bg='Yellow',
    fg='Blue',
    relief='groove',
    borderwidth=20,
    anchor='center',
    width=20,
    command=starter
)
start.place(y=520,x=88)

#Faz o loop infinito 
calculadora.mainloop()
