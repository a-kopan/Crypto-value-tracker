import json
import requests
def getApiData(time):
    #loading up the key from API_KEY.txt file
    API_KEY = open("src/API_KEY.txt","r").read()
    switcher = {
        "Today":1,
        "1 month":30,
        "3 months":90,
        "6 months":180,
        "1 year":365
    }
    #creating test request
    cryptoOfChoice = "DOGE"
    convertInto = "USD,EUR"
    convertInto = convertInto.split(",")
    prices = []
    for currency in convertInto:
        requestURL = f"https://min-api.cryptocompare.com/data/v2/histoday?fsym={cryptoOfChoice}&tsym={currency}&limit={switcher.get(time)}&api_key={API_KEY}"
        r = requests.get(requestURL)
        jsonrequest = r.json()
        data = jsonrequest.get("Data").get("Data")
        for x in data:
            prices.append((currency,(x.get("high"))))
    #prices = [x.get('high') for x in data]
    [print(x) for x in prices]
if __name__ == "__main__":
    print("MAIN: ",getApiData("1 month"))