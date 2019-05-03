from tkinter import *

class Window():
	def __init__(self,toplevel):
		self.fra = Frame(toplevel)
		self.fra.pack()
		self.botao = Button(self.fra, text='Hello World!',background='black',fg='white',height=4,width=10)
		#funcao compilar
		self.botao.pack(side='bottom')
		#print(self.botao)

raiz = Tk()
Window(raiz)
raiz.mainloop()