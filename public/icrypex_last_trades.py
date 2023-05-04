import requests
import json
import datetime
"""
url: Icrypex API adresi
API dokümantasyonu adresi: https://github.com/icrypex-com/apidoc
"""
url = "https://api.icrypex.com/v1/trades/last?symbol=BTCUSDT"


if __name__=="__main__":

    response = requests.request("GET", url)
    print(response.text)

