import requests
import random2

api_url  = "https://dummyjson.com/quotes"
response = requests.get(api_url)

def get_qoute():
    quote_data = response.json()
    qutoes_list = quote_data.get("quotes", [])
    random_quote = random2.choice(qutoes_list)
    final_quote = random_quote.get("quote", "No quote found.")
    author = random_quote.get("author", "Unknown")
    return f"{final_quote} - {author}"
print(get_qoute())


