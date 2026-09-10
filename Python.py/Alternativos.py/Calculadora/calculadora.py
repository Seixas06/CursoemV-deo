from tkinter import *
from defbotoes import *
from calculos import *

janela=Tk()
janela.title('Calculadora')
janela.geometry('600x700+625+100')
janela.resizable(False,False)
janela.config(bg='black')

for i in range(5):
    janela.columnconfigure(i,weight=1)
for i in range(7):
    janela.rowconfigure(i,weight=1)

entrada=Entry(janela,font=('arial',40),bg='black',fg='white',justify='right')
entrada.grid(row=0,column=0,rowspan=3,columnspan=5,sticky='nwse')


btn(janela,1,'blue',3,0,entrada)
btn(janela,2,'blue',3,1,entrada)
btn(janela,3,'blue',3,2,entrada)
btn(janela,4,'blue',4,0,entrada)
btn(janela,5,'blue',4,1,entrada)
btn(janela,6,'blue',4,2,entrada)
btn(janela,7,'blue',5,0,entrada)
btn(janela,8,'blue',5,1,entrada)
btn(janela,9,'blue',5,2,entrada)
bt0(janela,0,'blue',6,0,entrada)
bto(janela,'.','yellow',5,3,entrada)
bto(janela,'+','yellow',3,3,entrada)
bto(janela,'-','yellow',3,4,entrada)
bto(janela,'*','yellow',4,3,entrada)
bto(janela,'/','yellow',4,4,entrada)
btresult(janela,'=','yellow',5,4,entrada)
btreset(janela,'AC','yellow',6,3,entrada)
btdelet(janela,'⌫','yellow',6,2,entrada)



janela.mainloop()