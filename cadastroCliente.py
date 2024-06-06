from tkinter import *
from tkinter import messagebox

def confirma_info():
	messagebox.showwarning(title = "Fechou",message="Seus dados foram salvos.")
	

if __name__=='__main__':
    cadastro = Tk()



    #cadastro.configure(padx=30,pady=20)

    cadastro.title("Cadastro Cliente")


    menu = Frame(cadastro)
    menu.pack()
    
    dadosUser = Frame(cadastro)
    dadosUser.pack()

    
    


    progMenu = LabelFrame(menu)
    progMenu.grid(row=0,column=0)

    lblCadastro = Button(progMenu, text="Cadastro")
    lblPedidos = Button(progMenu,text="Pedidos")
    lblOpcao = Button(progMenu,text="Opções")
    lblClientes = Button(progMenu,text="Clientes")
    lblCadastro.grid(row=0,column=0)
    lblPedidos.grid(row=0,column=1)
    lblOpcao.grid(row=0,column=2)
    lblClientes.grid(row=0,column=3)



    dadoCliente = LabelFrame(dadosUser, text="Informações Cliente")
    dadoCliente.grid(row=1,column=0,pady=12)

    lblNome = Label(dadoCliente, text='Nome: ')
    lblNome.grid(row=0,column=0)
    Enome = Entry(dadoCliente)
    Enome.grid(row=0,column=1)

    lblIdade = Label(dadoCliente, text="Idade: ")
    spinIdade = Spinbox(dadoCliente, from_=18,to=90)
    lblIdade.grid(row=1,column=0)
    spinIdade.grid(row=1,column=1)

    lblCPF = Label(dadoCliente, text="CPF: ")
    ECPF = Entry(dadoCliente)
    lblCPF.grid(row=0,column=2)
    ECPF.grid(row=0,column=3)

    dadoContato = LabelFrame(dadosUser, text="Contato")
    dadoContato.grid(row=1, column=1, padx=20)

    lblCelular = Label(dadoContato, text="Celular: ")
    ECelular = Entry(dadoContato)
    lblWhatsApp= Label(dadoContato, text="Whats App: ")
    EWhats = Entry(dadoContato)
    lblCelular.grid(row=0,column=0)
    ECelular.grid(row=0,column=1)
    lblWhatsApp.grid(row=1,column=0)
    EWhats.grid(row=1,column=1)

    btnConfirma = Button(dadosUser, text="Confirmar", command=confirma_info)
    btnConfirma.grid(row=2,column=0)


    cadastro.mainloop()
