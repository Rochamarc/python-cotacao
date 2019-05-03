from tkinter import *
from api import *

class Packing:
    def __init__(self,tk_instance):
        #containers
        self.container1 = Frame(tk_instance)
        self.container2 = Frame(tk_instance)
        self.container3 = Frame(tk_instance)
        
        #packing
        self.container1.pack()
        self.container2.pack()
        self.container3.pack()

        #variables value
        self.dollar_value = f'R$ {GetDollar()}'
        self.dollar_variation = GetDollar('variation')
        self.euro_value = f'R$ {GetEuro()}'
        self.euro_variation = GetEuro('variation')
        self.peso_value = f'R$ {GetPeso()}'
        self.peso_variation = GetPeso('variation')
        self.bit_value = f'R$ {GetBitcoin()}'
        self.bit_variation = GetBitcoin('variation')

        #labels and buttons
        Label(self.container1, text='Cotações').pack(side=TOP)
        #Dollar
        Label(self.container2, text='Dollar').pack()
        Label(self.container2, text=self.dollar_value).pack()
        Label(self.container2, text=self.dollar_variation).pack()
        #Euro
        Label(self.container2, text='Euro').pack()
        Label(self.container2, text=self.euro_value).pack()
        Label(self.container2, text=self.euro_variation).pack()
        #Peso
        Label(self.container2, text='Peso').pack()
        Label(self.container2, text=self.peso_value).pack()
        Label(self.container2, text=self.peso_variation).pack()
        #Bitcoin
        Label(self.container2, text='Bitcoin')
        Label(self.container2, text=self.bit_value).pack()
        Label(self.container2, text=self.bit_variation).pack()
        #Reload bitcoins
        self.button_reload = Button(self.container3, text='Reload Coins',command=self.reload_api)
        self.button_reload.pack(side=LEFT)
        Button(self.container3, text='Plot Graphic').pack(side=LEFT)
        Button(self.container3, text='Exit').pack(side=LEFT)

    def reload_api():
        self.dollar_value = f'R$ {GetDollar()}'
        self.dollar_variation = GetDollar('variation')
        self.euro_value = f'R$ {GetEuro()}'
        self.euro_variation = GetEuro('variation')
        self.peso_value = f'R$ {GetPeso()}'
        self.peso_variation = GetPeso('variation')
        self.bit_value = f'R$ {GetBitcoin()}'
        self.bit_variation = GetBitcoin('variation')
        print(self.dollar_value, self.euro_value)

if __name__ == '__main__':
    raiz = Tk()
    Packing(raiz)
    raiz.mainloop()
