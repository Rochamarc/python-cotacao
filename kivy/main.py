from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from api import *

class Get_image (BoxLayout):

    def __init__(self):
        pass
    
    def GetDollarValue(self):
        return "R$ %.2f" %GetDollar()
    def GetDollarVariation(self):
        return GetDollar('variation')
    def GetPesoValue(self):
        return "R$ %.2f" %GetPeso() 
    def GetPesoVariation(self):
        return GetPeso('variation')
    def GetBitcoinValue(self):
        return "R$ %.2f" %GetBitcoin()
    def GetBitcoinVariation(self):
        return GetBitcoin('variation')
    def GetEuroValue(self):
        return "R$ %.2f" %GetEuro()
    def GetEuroVariation(self):
        return GetEuro("variation")
class Interface(App):

    def build(self):

        return Get_image()

Interface().run()
