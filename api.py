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

def GetDollar(type_="value",cot=cotacao):
    
    if type_ == 'value':
        return cot['USD']['buy']
    return cot['USD']['variation']        

def GetBitcoin(type_="value",cot=cotacao):
    
    if type_ == "value":
        return cot['BTC']['buy']
    return cot['BTC']['variation']

def GetEuro(type_="value",cot=cotacao):
    
    if type_ == "value":
        return cot['EUR']['buy']
    return cot['EUR']['variation']

def GetPeso(type_="value",cot=cotacao):
    
    if type_ == "value":
        return cot['ARS']['buy']
    return cot['ARS']['variation']
    

if __name__ == '__main__':
    dolar = GetDollar()
    print(dolar)
