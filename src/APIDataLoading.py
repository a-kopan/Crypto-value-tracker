import json
import requests
__name__ = "APIDataLoading"
cryptoOfChoice = "BTC"
convertInto = "USD"
keyFile = open("src/API_KEY.txt","r")
API_KEY = keyFile.read()
requestURL = f"https://min-api.cryptocompare.com/data/price?fsym={cryptoOfChoice}&tsyms={convertInto}&api_key={API_KEY}"
response = requests.get(requestURL)
data = json.dumps(response.json())