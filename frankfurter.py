def get_frankfurter_currency_list_endpoint():
    return "https://api.frankfurter.app/currencies"

def get_frankfurter_latest_endpoint(from_currency, to_currency):
    return f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}"

def get_frankfurter_historical_endpoint(from_currency, to_currency, date):
    return f"https://api.frankfurter.app/{date}?from={from_currency}&to={to_currency}"
