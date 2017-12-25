from tkinter import *
from src import binanceapi

def start():
    root = Tk()
    root.geometry("400x300")
    lab = Label(root)
    lab.pack()

    def refreshCoin():
        coinPrice = binanceapi.getCoinPrice('LTCUSDT')
        lab.config(text=coinPrice)
        # lab['text'] = time
        root.after(1000, refreshCoin)  # run itself again after 1000 ms

    # run first time
    refreshCoin()
    #my_gui = ArbyBotGUI(root)
    root.mainloop()