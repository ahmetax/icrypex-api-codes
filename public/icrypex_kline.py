import requests
import json
import datetime
"""
url: Icrypex API adresi
API dokümantasyonu adresi: https://github.com/icrypex-com/apidoc
"""
# url = "https://api.icrypex.com/sapi/v1/trades/kline"
url = "https://api.icrypex.com/v1/trades/kline"

resolution= 60  # 60 dakika
now=datetime.datetime.now()
t1=int(datetime.datetime.timestamp(now))
t0=t1-2*3600  # son 1 saat için. t0 değerini geri çekerek alınan kayıt sayısını arttırabilirsiniz
params={
    'symbol':'FTMUSDT',
    'resolution': resolution,
    'from': t0,
    'to': t1
}

if __name__=="__main__":

    response = requests.request("GET", url, params=params)
    if response:
        # print(response.text)
        print(response.json())
    else:
        print("Yanıt yok!")

