## import bibliotecas

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import banco


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

RightFrame = Frame(janela, width=398, height=500, bg="black", relief="raised")
RightFrame.pack(side=RIGHT)

Logo_Label = Label(LeftFrame, image=img_logo,bg="blue")
Logo_Label.place(x=50, y=100)

#inputs
User_Label = Label(RightFrame, text="Username", font=("Arial", 14), bg="black", fg="white")
User_Label.place(x=7, y=90)

User_Entry = Entry(RightFrame, width=18)
User_Entry.place(x=110, y=90)

Pass_Entry = Label(RightFrame, text="Password", font=("Arial", 14), bg="black", fg="white")
Pass_Entry.place(x=7, y=120)

Pass_Entry = Entry(RightFrame, width=18, show="*")
Pass_Entry.place(x=110, y=120)

#button
Login_Button = ttk.Button(RightFrame,text="login",width=18)
Login_Button.place(x=10, y=250)

#remove os butoons
def Cadastro():
    Login_Button.place(x=5000)
    Cad_Button.place(x=5000)
    
    Nome_Label = Label(RightFrame, text="Nome", font=("Arial", 14), bg="black", fg="white")
    Nome_Label.place(x=7, y=30)
    
    Nome_Entry = Entry(RightFrame, width=18, justify=CENTER)
    Nome_Entry.place(x=110, y=30)
    
    Email_Label = Label(RightFrame, text="E-mail", font=("Arial", 14), bg="black", fg="white")
    Email_Label.place(x=7, y=60)
    
    Email_Entry = Entry(RightFrame, width=18, justify=CENTER)
    Email_Entry.place(x=110, y=60)

    def Banco():
        Name = Nome_Entry.get()
        Email = Email_Entry.get()
        User = User_Entry.get()
        Pass = Pass_Entry.get()
        
        banco.cursor.execute("""
        INSERT INTO Users(Name, Email, User, Password) Values(?, ?, ?, ?)
        """,(Name, Email, User, Pass)) 

        banco.conn.commit()
        messagebox.showinfo(title="Info", message="O seu registro foi um sucesso!" )


    Cad= ttk.Button(RightFrame,text="Registrar",width=18, command=Banco)
    Cad.place(x=230, y=250)
    
    def Voltar():
    
       Nome_Label.place(x=5000)

       Nome_Entry.place(x=5000)

       Email_Label.place(x=5000)
       Email_Entry.place(x=5000)
       Back.place(x=5000)
       Cad.place(x=5000)

       #trazer de volta os buttons
       Login_Button.place(x=10, y=250)
       Cad_Button.place(x=230, y=250)

    Back = ttk.Button(RightFrame,text="Voltar",width=18, command=Voltar)
    Back.place(x=10, y=250)
    
    
Cad_Button = ttk.Button(RightFrame,text="cadastro",width=18, command=Cadastro)
Cad_Button.place(x=230, y=250)


janela.mainloop()