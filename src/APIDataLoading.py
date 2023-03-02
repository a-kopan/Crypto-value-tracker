import json
import requests
def getApiData():
    #loading up the key from API_KEY.txt file
    keyFile = open("src/API_KEY.txt","r")
    API_KEY = keyFile.read()
    #creating test request
    cryptoOfChoice = "DOGE"
    convertInto = "USD,EUR"
    #functions for specific scenarios
    def getToday(cryptoOfChoice,convertInto):
        requestURL = f"https://min-api.cryptocompare.com/data/price?fsym={cryptoOfChoice}&tsyms={convertInto}&api_key={API_KEY}"
        response = requests.get(requestURL)
        data = json.dumps(response.json())
        return data 
    def getFromMonth(cryptoOfChoice,convertInto):
        requestURL = f""
    print(getToday(cryptoOfChoice,convertInto))
if __name__ == "__main__":
    getApiData()