from tkinter import *
from PIL import Image,ImageTk
from facitk import imagem

def np():
    for widget in vector.winfo_children():
        widget.destroy()
    vector.grid_columnconfigure(1,minsize=5)
    vector.grid_columnconfigure(3,minsize=20,weight=5)
    vector.grid_columnconfigure(4,minsize=40)
    vector.grid_rowconfigure(6,minsize=90)
    
    win1= Label(vector, image=vezin1)
    win1.grid(row=4,column=3)
    
    win2= Label(vector, image=vezin2)
    win2.grid(row=5,column=2)
    
    win3= Label(vector, image=vezin3)
    win3.grid(row=5,column=5)
    
    frase1=Label(
        vector, 
        text='Victor Alves\nO rei da BANANA',
        bg='yellow',
        fg='blue',
        font=('cinzel',20),
        width=15,
        height=5,
        relief='sunken',
        borderwidth=20
        )
    frase1.grid(row= 5,column=3)
         

vector=Tk()
vector.title('VECTOR')
vector.geometry('1200x800+335+100')
vector.iconbitmap('favicon (1).ico')
vector.config(bg='lightblue')
vector.resizable(True,True)
vector.grid_rowconfigure(3, minsize=80,)
vector.grid_rowconfigure(3, minsize=80,)
vector.grid_columnconfigure(1, minsize=200,weight=2)
vector.grid_columnconfigure(2, minsize=200,weight=5)
vector.grid_columnconfigure(3, minsize=5,weight=50)

trya= Image.open('VezinMao.jpeg').resize((300, 300))
vezin1 = ImageTk.PhotoImage(trya)

tryb= Image.open('VezinMacaco.jpeg').resize((300, 300))
vezin2 = ImageTk.PhotoImage(tryb)

tryc= Image.open('VezinChild.jpeg').resize((300, 300))
vezin3 = ImageTk.PhotoImage(tryc)

tryd= Image.open('MacacoBanana.jpg').resize((250, 250))
monkey1 = ImageTk.PhotoImage(tryd)

trye= Image.open('MacacoPensando.jpg').resize((250, 250))
monkey2 = ImageTk.PhotoImage(trye)

win4= Label(vector, image=monkey1)
win4.grid(row=4,column=1)
    
win5= Label(vector, image=monkey2)
win5.grid(row=4,column=4)

titulo=Label(
    vector,
    text='Você conhece esse cara?\nBanana Rei!',
    font=('cinzel',30),
    fg='white',
    width=49,
    height=5,
    bg='blue',
    borderwidth=30,
    relief='sunken'
    )
titulo.grid(column=1,row=1,columnspan=4,rowspan=2)

botao=Button(
    vector,
    text='Clique para descobrir!',
    width=20,
    height=2,
    fg='blue',
    bg='yellow',
    font=('cinzel',30),
    relief='ridge',
    anchor='center',
    borderwidth=30,
    command=np
    )
botao.grid(row=4,column=2,padx=100,columnspan=2)

vector.mainloop()
