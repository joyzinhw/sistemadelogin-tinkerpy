## import bibliotecas

from tkinter import *
from tkinter import messagebox
from tkinter import ttk


janela = Tk()
janela.title("login")
janela.geometry("600x300")
janela.configure(background="white")
janela.resizable(width=False, height=False)
janela.attributes("-alpha", 0.9)

img_logo = PhotoImage(file="imagem/asa.png")

#desing da janela e tamanho

LeftFrame = Frame(janela, width=200, height=300, bg="blue", relief="raised")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(janela, width=398, height=300, bg="black", relief="raised")
RightFrame.pack(side=RIGHT)

#inputs

Logo_Label = Label(LeftFrame, image=img_logo,bg="blue")
Logo_Label.place(x=50, y=100)

User_Label = Label(RightFrame, text="Username", font=("Arial", 14), bg="black", fg="white")
User_Label.place(x=7, y=100)

User_Entry = Entry(RightFrame, width=18)
User_Entry.place(x=110, y=100)

Pass_Entry = Label(RightFrame, text="Password", font=("Arial", 14), bg="black", fg="white")
Pass_Entry.place(x=7, y=140)

Pass_Entry = Entry(RightFrame, width=18)
Pass_Entry.place(x=110, y=140)

#button
Login_Button = ttk.Button(RightFrame,text="login",width=16)
Login_Button.place(x=10, y=250)

Cad_Button = ttk.Button(RightFrame,text="cadastro",width=16)
Cad_Button.place(x=245, y=250)


janela.mainloop()