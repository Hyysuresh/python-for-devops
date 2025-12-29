import requests
API_KEY = "ZIO61XS69E6E82B3"
SYMBOL="IBM"
function = 'TIME_SERIES_WEEKLY_ADJUSTED'
api_url = 'https://www.alphavantage.co/'
query = f"query?function={function}&symbol={SYMBOL}&apikey={API_KEY}"
response = requests.get(url = api_url + query )

def get_stock_data():
    for key, value in response.json().items():
        if key == "Meta Data":
            symbol = value.get("2. Symbol", "No symbol found.")   
        if key == "Weekly Adjusted Time Series":
            dates = value.get(date, {})
            Market_date = date
            open_price = dates.get("1. open", "No open price found.")
            high_price = dates.get("2. high", "No high price found.")
            low_price = dates.get("3. low", "No low price found.")
            close_price = dates.get("4. close", "No close price found.")
            volume = dates.get("6. volume", "No volume found.")
    return f"Symbol: {symbol}\nMarket_Date: {Market_date}\nOpen Price: {open_price}\nHigh Price: {high_price}\nLow Price: {low_price}\nClose Price: {close_price}\nVolume: {volume}"
date =input("Enter the date to get stock data: ")
print(get_stock_data())
