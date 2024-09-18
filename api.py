import requests
from frankfurter import get_frankfurter_latest_endpoint, get_frankfurter_historical_endpoint, get_frankfurter_currency_list_endpoint

def get_currency_codes():
    endpoint = get_frankfurter_currency_list_endpoint()
    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            return list(response.json().keys())  # Return the currency codes
        else:
            return []
    except Exception as e:
        print(f"Error fetching currency codes: {e}")
        return []

def get_conversion_rate(from_currency, to_currency, date=None):
    if date:
        endpoint = get_frankfurter_historical_endpoint(from_currency, to_currency, date)
    else:
        endpoint = get_frankfurter_latest_endpoint(from_currency, to_currency)
    
    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            data = response.json()
            return data['rates'].get(to_currency)
        else:
            return None
    except Exception as e:
        print(f"Error fetching conversion rate: {e}")
        return None
