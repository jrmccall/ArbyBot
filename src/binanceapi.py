from binance.client import Client

api_key = 'DVzJxwToIDoEyYKDXYwRRSXfAePFftU9iySjnb2ouARwyeuxZN0hVUeyF2sS1rbk'
api_secret = '86qb9XwzIETqzt8ULLZRrjkn4WAZSshKNcdL7CUjEfdiZj4gNNXrj2tNICVXLhnK'

client = Client(api_key, api_secret)

client.ping()


def getCoinPrice(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    price = ticker.get('price')
    return price


BTCRATE = getCoinPrice('BTCUSDT')
ETHRATE = getCoinPrice('ETHUSDT')
BTCRATE = getCoinPrice('BNBUSDT')


def getLastPrice(symbol):
    ticker = client.get_ticker(symbol=symbol)
    lastPrice = ticker.get('lastPrice')

    return lastPrice

# SAVED FOR EXAMPLE PURPOSES
# for ticker in tickers:
#     print(ticker)
#     if ticker.get('symbol') == 'LTCUSDT':
#         ltcusdt = ticker
# print(tickers[0].get('symbol'))

hello = 2



