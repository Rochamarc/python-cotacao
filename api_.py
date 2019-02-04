import requests
import json

req = None
try:
    req = requests.get("https://api.hgbrasil.com/finance/quotations?format=json&key=5c88539b")
except:
    print("Erro na conexão")
    exit()

cotacao = json.loads(req.text)
cotacao = cotacao['results']['currencies']

def GetDollar(type_="value"):
    
    global cotacao 
    if type_ == 'value':
        return "R$ %.2f" %cotacao['USD']['buy']
    return cotacao['USD']['variation']        

def GetBitcoin(type_="value"):
    
    global cotacao
    if type_ == "value":
        return "R$ %.2f" %cotacao['BTC']['buy']
    return cotacao['BTC']['variation']

def GetEuro(type_="value"):
    
    global cotacao
    if type_ == "value":
        return "R$ %.2f" %cotacao['EUR']['buy']
    return cotacao['EUR']['variation']

def GetPeso(type_="value"):
    
    global cotacao
    if type_ == "value":
        return "R$ %.2f" %cotacao['ARS']['buy']
    return cotacao['ARS']['variation']
    
