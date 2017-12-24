import json
from binance.client import Client
import Tkinter as tk

api_key = 'DVzJxwToIDoEyYKDXYwRRSXfAePFftU9iySjnb2ouARwyeuxZN0hVUeyF2sS1rbk'
api_secret = '86qb9XwzIETqzt8ULLZRrjkn4WAZSshKNcdL7CUjEfdiZj4gNNXrj2tNICVXLhnK'

client = Client(api_key, api_secret)

client.ping()

def getCoinPrice(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    price = ticker.get(u'price')
    return price

tickers = client.get_all_tickers()

# SAVED FOR EXAMPLE PURPOSES
# for ticker in tickers:
#     if ticker.get(u'symbol') == 'LTCUSDT':
#         ltcusdt = ticker
# print(tickers[0].get(u'symbol'))

BTCrate = getCoinPrice('BTCUSDT')
ETHrate = getCoinPrice('ETHUSDT')
BTCrate = getCoinPrice('BNBUSDT')

print getCoinPrice('LTCUSDT')
print getCoinPrice('LTCBTC')
print getCoinPrice('LTCETH')
print getCoinPrice('LTCBNB')


# root = tk.Tk()
#
# text = Text(root)
#
# root.mainloop()



