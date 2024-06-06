import tkinter
from tkinter import *

if __name__=='__main__':
	pedido = Tk()
	pedido.title("Pedidos")
	menu = Frame(pedido)
	menu.pack()

	#Frame do menu
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

	#Frame do conteudo da página
	infor = Frame(pedido)
	infor.pack()

	dadoPedido = LabelFrame(infor, text="Informações da Compra")
	dadoPedido.grid(row=1,column=0,padx=12)
	
	lblNomeCliente = Label(dadoPedido, text="Nome: ")
	Enome = Entry(dadoPedido)
	lblNomeCliente.grid(row=0,column=0)
	Enome.grid(row=0,column=1)

	lblNumPedido = Label(dadoPedido, text="Nº Pedido: ")
	ENum = Entry(dadoPedido)
	lblNumPedido.grid(row=0,column=2)
	ENum.grid(row=0,column=3)

	





	pedido.mainloop()