var dolar = document.getElementById('dolar');
var euro = document.getElementById('euro');
var peso = document.getElementById('peso');
var bitcoin = document.getElementById('bitcoin');
var dolarValue = document.createElement('li');
var euroValue= document.createElement('li');
var pesoValue = document.createElement('li');
var bitcoinValue = document.createElement('li');


//facilitando a nossa vida
axios.get("https://api.hgbrasil.com/finance?format=json-cors&key=5c88539b")
    .then(function(response){
        //busco o valor na biblioteca
        var textDolar = document.createTextNode(String(response.data.results.currencies.USD.buy));
        var textEuro = document.createTextNode(String(response.data.results.currencies.EUR.buy));
        var textPeso = document.createTextNode(String(response.data.results.currencies.ARS.buy));
        var textBitcoin = document.createTextNode(String(response.data.results.currencies.BTC.buy));
        //linko dentro do li que foi criado
        dolarValue.appendChild(textDolar);
        euroValue.appendChild(textEuro);
        pesoValue.appendChild(textPeso);
        bitcoinValue.appendChild(textBitcoin);
        
        //linko o que foi criado dentro das divs das moedas
        dolar.appendChild(dolarValue);
        euro.appendChild(euroValue);
        peso.appendChild(pesoValue);
        bitcoin.appendChild(bitcoinValue);
    })
    .catch(function(erro){
        console.warn(error);
    });
