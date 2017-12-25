from tkinter import *
from src import binanceapi

from tkinter import Tk, Label, Button, StringVar

def start():
    root = Tk()
    root.geometry("400x300")
    Lltcusdt = Label(root)
    Lltcusdt.pack()
    Lltcbtc = Label(root)
    Lltcbtc.pack()

    def refreshCoin():
        ltcusdt = binanceapi.getCoinPrice('LTCUSDT')
        ltcbtc = round(binanceapi.getCoinPrice('LTCBTC') * binanceapi.getCoinPrice('BTCUSDT'), 4)
        ltceth = round(binanceapi.getCoinPrice('LTCETH') * binanceapi.getCoinPrice('ETHUSDT'), 4)
        ltcbnb = round(binanceapi.getCoinPrice('LTCBNB') * binanceapi.getCoinPrice('BNBUSDT'), 4)

        iotausdt = binanceapi.getCoinPrice('IOTAUSDT')
        iotabtc = round(binanceapi.getCoinPrice('IOTABTC') * binanceapi.getCoinPrice('BTCUSDT'), 4)
        iotaeth = round(binanceapi.getCoinPrice('IOTAETH') * binanceapi.getCoinPrice('ETHUSDT'), 4)
        iotabnb = round(binanceapi.getCoinPrice('IOTABNB') * binanceapi.getCoinPrice('BNBUSDT'), 4)

        bccusdt = binanceapi.getCoinPrice('BCCUSDT')
        bccbtc = round(binanceapi.getCoinPrice('BCCBTC') * binanceapi.getCoinPrice('BTCUSDT'), 4)
        bcceth = round(binanceapi.getCoinPrice('BCCETH') * binanceapi.getCoinPrice('ETHUSDT'), 4)
        bccbnb = round(binanceapi.getCoinPrice('BCCBNB') * binanceapi.getCoinPrice('BNBUSDT'), 4)
        # coinPrices = binanceapi.getAllTickers()
        # for coinPrice in coinPrices:
        #     T.insert(END, coinPrice['symbol'] + ": " + coinPrice['price'] +"\n")
        Lltcusdt.config(text=ltcusdt)
        Lltcbtc.config(text=ltcbtc)
        root.after(1000, refreshCoin)  # run itself again after 1000 ms

    # run first time
    refreshCoin()
    #my_gui = ArbyBotGUI(root)
    root.mainloop()