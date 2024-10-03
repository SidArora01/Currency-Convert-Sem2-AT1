import json
from api import get_url

# Define endpoint functions
def get_frankfurter_currency_list_endpoint():
    return "https://api.frankfurter.app/currencies"

def get_frankfurter_latest_endpoint(from_currency, to_currency):
    return f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}"

def get_frankfurter_historical_endpoint(from_currency, to_currency, date):
    return f"https://api.frankfurter.app/{date}?from={from_currency}&to={to_currency}"

# Define main functions for currency data
def get_currencies_list():
    """
    Function that calls the relevant API endpoint to get the list of available currencies.
    """
    url = get_frankfurter_currency_list_endpoint()
    status_code, response = get_url(url)  # Unpack the response

    if status_code == 200:
        try:
            return json.loads(response)  # Return parsed JSON response
        except json.JSONDecodeError:
            return None
    else:
        return None

def get_latest_rates(from_currency, to_currency, amount):
    """
    Get the latest conversion rate between the provided currencies.
    """
    url = get_frankfurter_latest_endpoint(from_currency, to_currency)
    status_code, response = get_url(url)  # Unpack the response

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

def get_historical_rate(from_currency, to_currency, from_date, amount):
   
    url = get_frankfurter_historical_endpoint(from_currency, to_currency, from_date)
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
        
