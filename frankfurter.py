import json
from api import get_url

#Base URL defined here as it is the common API part, helps ensure maintainence and consistency
BASE_URL = "https://api.frankfurter.app"


#Fetches the list of Currencies from the API Endpoint
def get_currencies_list():
    url = f"{BASE_URL}/currencies"
    status_code, response = get_url(url)  

    if status_code == 200:
        try:
            return list(json.loads(response).keys())
        except json.JSONDecodeError:
            return None
    else:
        return None


#Fetches Latest Exchnage Rates from given pair of Currencies
#Error Handling done in try and except blocks
def get_latest_rates(from_currency, to_currency, amount):
    url = f"{BASE_URL}/latest?from={from_currency}&to={to_currency}"
    status_code, response = get_url(url)

    if status_code == 200:
        try:
            data = json.loads(response)
            date = data['date']
            rate = data['rates'][to_currency]
            return date, rate
        except (json.JSONDecodeError, KeyError):
            return None, None
    else:
        return None, None


#Fetches Exchnage Rates from given pair of Currencies for a given date in the past
#Error Handling done in try and except blocks
def get_historical_rate(from_currency, to_currency, from_date, amount):
    url = f"{BASE_URL}/{from_date}?from={from_currency}&to={to_currency}"
    status_code, response = get_url(url)  

    if status_code == 200:
        try:
            data = json.loads(response)
            rate = data['rates'][to_currency]
            print(rate)
            return rate
        except (json.JSONDecodeError, KeyError):
            return None
    else:
        return None
        
