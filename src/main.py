import drawGraph
import APIDataLoading
import tkinter as tk 
from tkinter import messagebox,ttk
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        #window config
        self.title("Main menu")
        self.geometry("300x150")
        #ADDING WIDGETS
        #label and entry for input
        inputLabel = ttk.Label(self, text="Input shortcuts for cryptocurrencies: (ex. btc,eth,...)"); inputLabel.pack()
        inputEntry = ttk.Entry(self); inputEntry.pack()
        #label and entry for input
        outputLabel = ttk.Label(self, text="Output shortcuts for cryptocurrencies: (ex. btc, eth)"); outputLabel.pack()
        outputEntry = ttk.Entry(self); outputEntry.pack()
        #label and selector for time interval
        choices = ["1 year", "6 months", "3 months", "1 months", "1 day"]
        timeSelectorLabel = ttk.Label(self, text="Choose time interval for data output:"); timeSelectorLabel.pack()
        timeSelector = ttk.Combobox(self, values = choices); timeSelector.pack()

if __name__=="__main__" :
    app = MainApp()
    app.mainloop()