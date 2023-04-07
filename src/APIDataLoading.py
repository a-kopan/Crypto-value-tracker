import json
import requests
def getApiData(time, cryptoOfChoice, convertInto):
    #loading up the key from API_KEY.txt file
    API_KEY = open("src/API_KEY.txt","r").read()
    #check if input is an number
    try:
        time = int(time)
    except:
        return []
    
    listOfConvertFrom = cryptoOfChoice.split(",")
    
    
    objArray = dict()
    for currency in listOfConvertFrom:
        requestURL = f"https://min-api.cryptocompare.com/data/v2/histoday?fsym={currency}&tsym={convertInto}&limit={time}&api_key={API_KEY}"
        loadedData = requests.get(requestURL)
        apiOutput = loadedData.json()
        dataArray = apiOutput.get("Data").get("Data")
        counter = 0
        for element in dataArray:
            holder = {currency:element.get("high")}
            objArray.setdefault(str(counter), dict()).update(holder)
            counter+=1
    return objArray

if __name__ == "__main__":
    test = getApiData(5,"DOGE,BTC","USD")
    keySet = test.keys()
    for key in keySet:
        print(key+" : "+str(test[key]))
    