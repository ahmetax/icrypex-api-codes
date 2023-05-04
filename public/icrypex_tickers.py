import requests
import json
import datetime
"""
url: Icrypex API adresi
API dokümantasyonu adresi: https://github.com/icrypex-com/apidoc
"""
url = "https://api.icrypex.com/v1/tickers"


# Listelenmesi istenen çiftler
symbols1=["USDT/TRY",
         "BTC/USDT",
         "ETH/USDT",
         "FTM/USDT",
         "AVAX/USDT",
         "ALTAY/USDT",
         "ALTAY/TRY",
         "HOT/USDT",
         "ALGO/USDT",
         "XLM/USDT",
         "DOT/USDT",
         "SHIB/USDT",
         "XRP/USDT",
         "CEEK/USDT",
         "BAT/USDT",
         "LOVELY/USDT"
         ]

# çiftlerin para birimi / ile ayrılmışsa kaldırılıyor. 
# Çünkü Icrypex API'sinde çiftler birleşik tanımlanmış 
symbols=[]
for s in symbols1:
    symbols.append(s.replace('/',''))
params={}

def get_all_icrypex_prices(pkodlar):
    """
    pkodlar: boş bir sözlük (dict)
    Elde edilen bilgiler bu değişkene aktarılarak geri döndürülüyor.
    """
    response = requests.request("GET", url, params=params)
    if response:
        # print(response.json())
        liste = json.loads(response.text)
        for l in liste:
            if l['symbol'] in symbols:
                # Örnek olarak sembol(symbol), son fiyat(last) ve değişim(change) değerleri print ediliyor
                # Kayıt yapısına ait ayrıntıları aşağıdaki API dokümantasyonunda bulabilirsiniz
                # https://github.com/icrypex-com/apidoc/blob/main/trading-public.md#tickers
                print(f"{l['symbol']:10} {float(l['last']):20.10f} {float(l['change']):6.2f}")
                s=l['symbol']
                if 'TRY' in s:
                    s=s[:len(s)-3]+'/'+'TRY'
                elif 'USDT' in s:
                    s=s[:len(s)-4]+'/'+'USDT'

                pkodlar[s]=float(l['last'])

    else:
        print("Yanıt yok!")
    return pkodlar

if __name__=="__main__":
    pkodlar = {}
    pkodlar = get_all_icrypex_prices(pkodlar)
    print(pkodlar)

