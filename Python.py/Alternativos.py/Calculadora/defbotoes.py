from tkinter import *
from estado import *


def btn(jn,num,cf,rw,clm,entrada):
    btn=Button(
    jn,
    text=str(num),
    bg=cf,
    fg='yellow',
    width=10,
    height=4,
    font=('arial',15),
    command=lambda: adicionar(str(num),entrada)
    )
    btn.grid(row=rw,column=clm,sticky='nwse')
    
    
    
def bto(jn,num,cf,rw,clm,entrada):
    btn=Button(
    jn,
    text=num,
    bg=cf,
    fg='blue',
    width=10,
    height=4,
    font=('arial',15),
    command=lambda:adicionar(num,entrada)
    )
    btn.grid(row=rw,column=clm,sticky='nwse')




def btresult(jn,num,cf,rw,clm,entrada):
    btn=Button(
    jn,
    text=num,
    bg=cf,
    fg='blue',
    width=10,
    height=4,
    font=('arial',15),
    command=lambda:resultado(entrada)
    )
    btn.grid(row=rw,column=clm,sticky='nwse',rowspan=2)



def bt0(jn,num,cf,rw,clm,entrada):
    btn=Button(
    jn,
    text=num,
    bg=cf,
    fg='white',
    width=1,
    height=4,
    font=('arial',15),
    command=lambda: adicionar(str(num),entrada)
    )
    btn.grid(row=rw,column=clm,sticky='nwse',columnspan=2)



def btreset(jn,num,cf,rw,clm,entrada):
    btn=Button(
    jn,
    text=num,
    bg=cf,
    fg='blue',
    width=10,
    height=4,
    font=('arial',15),
    command=lambda:limpar(entrada)
    )
    btn.grid(row=rw,column=clm,sticky='nwse')



def btdelet(jn,num,cf,rw,clm,entrada):
    btn=Button(
    jn,
    text=num,
    bg=cf,
    fg='blue',
    width=10,
    height=4,
    font=('arial',15),
    command=lambda:apagar(entrada)
    )
    btn.grid(row=rw,column=clm,sticky='nwse')

