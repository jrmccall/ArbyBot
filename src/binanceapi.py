from binance.client import Client

api_key = 'GOES HERE'
api_secret = 'GOES HERE'

client = Client(api_key, api_secret)

client.ping()


def getCoinPrice(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    price = ticker.get('price')
    return float(price)


BTCRATE = getCoinPrice('BTCUSDT')
ETHRATE = getCoinPrice('ETHUSDT')
BNBRATE = getCoinPrice('BNBUSDT')


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

def makeOrderTEST(symbol, side, quantity):
    #todo: Get symbol, side, and quantity returning from some decision making, maybe do decision making in this function?
    price = getLastPrice(symbol)
    client.create_test_order(symbol=symbol, side=side, quantity=quantity, price=price)

def checkPair(symbol):
    usdt = getCoinPrice(symbol=symbol+'USDT')
    btc = getCoinPrice(symbol=symbol+'BTC')
    eth = getCoinPrice(symbol=symbol+'ETH')
    bnb = getCoinPrice(symbol=symbol+'BNB')

    # if usdt < btc:
    #     if (btc - usdt)/usdt < 0.2:



# SAVED FOR EXAMPLE PURPOSES
# for ticker in tickers:
#     print(ticker)
#     if ticker.get('symbol') == 'LTCUSDT':
#         ltcusdt = ticker
# print(tickers[0].get('symbol'))