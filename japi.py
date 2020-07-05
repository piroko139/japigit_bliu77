import json
import urllib.request

symbol = 'x'

##Takes a stock's symbol as a parameter and convert the response from JSON into a Python dictionary
def getStockData(symbol):
    url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + symbol + '&apikey=55I6CI0C5EYP5SQ1'
    json_obj = urllib.request.urlopen(url)
    data = json.load(json_obj)
    return data


f = open('japi.out','a')
 
##Ask the user for a new stock symbol until the user enters quit
while symbol != 'quit':

    ##Get symbol
    symbol = input('Enter the stock symbol for the company you want to see: ')

    if symbol == 'quit':
        break
    ##Pass symbol to getStockData
    newData = getStockData(symbol)

    ##Print the JSON-formated response
    print(newData, file=f)

    ##Print the price ONLY
    print('The current price of ' + newData['Global Quote']['01. symbol'] + ' is: ' + newData['Global Quote']['05. price'], file=f)

f.close()

print("Stock Quotes retrieved successfully!")
