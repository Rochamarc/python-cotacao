import requests
import json

req = None
try:
    req = requests.get("https://api.hgbrasil.com/finance/quotations?format=json&key=5c88539b")
except:
    print("Erro na conexão")
    exit()

cotacao = json.loads(req.text)

def GetDollar(type_):
    
    global cotacao
    dollar = cotacao['results']['currencies']['USD']
    dollar_value = dollar['buy']
    dollar_variation = dollar['variation']
    if type_ == 'value':
        return "R$ %.2f" %dollar_value
    return dollar_variation        

def GetBitcoin(type_):
    
    global cotacao
    bitcoin = cotacao['results']['currencies']['BTC']
    bitcoin_value = bitcoin['buy']
    bitcoin_variation = bitcoin['variation']
    if type_ == "value":
        return "R$ %.2f" %bitcoin_value
    return bitcoin_variation

def GetEuro(type_):
    
    global cotacao
    euro = cotacao['results']['currencies']['EUR']
    euro_value = euro['buy']
    euro_variation = euro['variation']
    if type_ == "value":
        return "R$ %.2f" %euro_value
    return euro_variation

def GetPeso(type_):
    
    global cotacao
    peso = cotacao['results']['currencies']['ARS']
    peso_value = peso['buy']
    peso_variation = peso['variation']
    if type_ == "value":
        return "R$ %.2f" %peso_value
    return peso_variation
    
