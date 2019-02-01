from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from api_ import GetBitcoin, GetDollar, GetEuro, GetPeso

class Get_image (BoxLayout):

    def GetDollarValue(self):
        return GetDollar("value")
    def GetDollarVariation(self):
        return GetDollar('variation')
    def GetPesoValue(self):
        return GetPeso("value") 
    def GetPesoVariation(self):
        return GetPeso('variation')
    def GetBitcoinValue(self):
        return GetBitcoin("value")
    def GetBitcoinVariation(self):
        return GetBitcoin('variation')
    def GetEuroValue(self):
        return GetEuro("value")
    def GetEuroVariation(self):
        return GetEuro("variation")

class Interface(App):

    def build(self):

        return Get_image()

Interface().run()