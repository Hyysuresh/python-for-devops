import requests

api_url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(api_url)
print(type(response.json()))

def get_joke():
    joke_data = response.json()
    type_of_joke = joke_data.get("type", "unkown")
    setup = joke_data.get("setup", "No setup available")
    joke_id = joke_data.get("id", "no id")
    punchline = joke_data.get("punchline", "No punchline available")    
    return f" joke_type: {type_of_joke} joke_id: {joke_id}  joke: {setup} - {punchline}"

print(get_joke())
