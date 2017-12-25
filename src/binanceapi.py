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

def getAllTickers():
    tickers = client.get_all_tickers()
    #Sort tickers
    sorted_tickers = sorted(tickers, key=lambda ticker: ticker['symbol'])
    for ticker in sorted_tickers:
        print(ticker['symbol'] + ": " + ticker['price'])
    return sorted_tickers

hello = 2



# SAVED FOR EXAMPLE PURPOSES
# for ticker in tickers:
#     print(ticker)
#     if ticker.get('symbol') == 'LTCUSDT':
#         ltcusdt = ticker
# print(tickers[0].get('symbol'))