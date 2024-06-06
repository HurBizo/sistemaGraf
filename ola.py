from tkinter import *

def somar():
    print("foda-se")


if __name__=='__main__':
    window = Tk()

    window.title("Programa")
    frame = Frame(window)
    frame.pack()

    dados = LabelFrame(frame,text="Dados usuário",padx=10,pady=10)
    dados.grid(row=0,column=0,padx=50,pady=10)
    
    lblValor1 = Label(dados, text="Numero1: ")
    lblValor1.grid(row=0,column=0)
    EValor1 = Entry(dados)
    EValor1.grid(row=0,column=1)
    lblValor2 = Label(dados, text="Número2: ")
    lblValor2.grid(row=1,column=0)
    EValor2 = Entry(dados)
    EValor2.grid(row=1, column=1)
   
    btnConfirmar = Button(dados, text="Confirmar", command=somar)
    btnConfirmar.grid(row=2,column=1,pady=20)

    window.mainloop()

