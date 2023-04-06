import drawGraph
import APIDataLoading
import tkinter as tk
from tkinter import messagebox,ttk

def submitDate(date,input,output):
    print(APIDataLoading.getApiData(date,input,output))
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        menuFrame = tk.Frame(self)
        #window config
        self.title("Main menu")
        self.geometry("600x300")
        #ADDING WIDGETS
        #label and entry for input
        inputLabel = ttk.Label(menuFrame, text="Input shortcuts for cryptocurrencies: (ex. btc,eth,...)"); 
        inputLabel.pack()
        inputEntry = ttk.Entry(menuFrame); 
        inputEntry.pack()
        #label and entry for input
        outputLabel = ttk.Label(menuFrame, text="Output shortcuts for cryptocurrencies: (ex. btc, eth)"); 
        outputLabel.pack()
        outputEntry = ttk.Entry(menuFrame); 
        outputEntry.pack()
        #label and selector for time interval
        choosenDate = tk.StringVar()
        choosenDate.set("Today")
        timeSelectorLabel = ttk.Label(menuFrame, text="Choose time interval for data output:"); 
        timeSelectorLabel.pack()
        timeSelector = tk.OptionMenu(menuFrame,choosenDate, *["1 year", "6 months", "3 months", "1 month", "Today"]);
        timeSelector.pack()
        #generate button
        submitButton = ttk.Button(menuFrame,
                                  text="Show graph",
                                  command=lambda: submitDate(choosenDate.get(),
                                                             inputEntry.get(),
                                                             outputEntry.get())
                                  )
        submitButton.pack()
        menuFrame.pack()
        
if __name__=="__main__" :
    app = MainApp()
    app.mainloop()          