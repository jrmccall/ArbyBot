from tkinter import *
from src import binanceapi

from tkinter import Tk, Label, Button, StringVar

def start():
    root = Tk()
    root.geometry("600x300")
    coinlabel = Label(text = "COIN")
    usdlabel = Label(text = "Dollar Value in\nUSDT")
    btclabel = Label(text = "Dollar Value in\nBTC")
    ethlabel = Label(text="Dollar Value in\nETH")
    bnblabel = Label(text="Dollar Value in\nBNB")
    Lltcprice = Label(text="LTC")
    Liotaprice = Label(text="IOTA")
    Lbccprice = Label(text="BCC")

    Lltcusdt= Label(root)
    Lltcbtc = Label(root)
    Lltceth = Label(root)
    Lltcbnb = Label(root)

    Liotabtc = Label(root)
    Liotaeth = Label(root)
    Liotabnb = Label(root)

    Lbccusdt= Label(root)
    Lbccbtc = Label(root)
    Lbcceth = Label(root)
    Lbccbnb = Label(root)


    btclabel.grid(row=0, column=3, sticky=W+E, padx=6)
    ethlabel.grid(row=0, column=4, sticky=W+E, padx=6)
    bnblabel.grid(row=0, column=5, sticky=W+E, padx=6)

    Lltcusdt.grid(row=1, column=2, sticky=W+E, padx=6, pady=6)
    Lltcprice.grid(row=1, column=1, sticky=W+E, padx=6, pady=6)
    Lbccprice.grid(row=2, column=1, sticky=W+E, padx=6, pady=6)
    Liotaprice.grid(row=3, column=1, sticky=W+E, padx=6, pady=6)

    def refreshCoin():
        ltcusdt = binanceapi.getCoinPrice('LTCUSDT')
        ltcbtc = round(binanceapi.getCoinPrice('LTCBTC') * binanceapi.getCoinPrice('BTCUSDT'), 4)
        ltceth = round(binanceapi.getCoinPrice('LTCETH') * binanceapi.getCoinPrice('ETHUSDT'), 4)
        ltcbnb = round(binanceapi.getCoinPrice('LTCBNB') * binanceapi.getCoinPrice('BNBUSDT'), 4)

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
        Lltcbtc.config(text=ltcusdt)
        Lltceth.config(text=ltcusdt)
        Lltcbnb.config(text=ltcusdt)

        Liotabtc.config(text=ltcusdt)
        Liotaeth.config(text=ltcusdt)
        Liotabnb.config(text=ltcusdt)

        Lbccusdt.config(text=ltcusdt)
        Lbccbtc.config(text=ltcusdt)
        Lbcceth.config(text=ltcusdt)
        Lbccbnb.config(text=ltcusdt)

        root.after(1000, refreshCoin)  # run itself again after 1000 ms

    # run first time
    refreshCoin()
    #my_gui = ArbyBotGUI(root)
    root.mainloop()