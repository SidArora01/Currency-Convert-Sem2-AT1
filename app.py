import streamlit as st
from api import get_url  
from frankfurter import get_latest_rates, get_historical_rate, get_currencies_list  
from currency import format_currency, round_rate, reverse_rate  
from datetime import date
import json


def fetch_currency_codes():
    currencies = get_currencies_list()
    if currencies:
        return list(currencies.keys())
    return []


available_currencies = fetch_currency_codes()

UTS_logo = "UTS-logo.jpg"
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(UTS_logo, use_column_width=True)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.title("Currency Converter")
    st.subheader("BY: Siddharth Arora (25106954)")


amount = st.number_input("Enter the amount to convert", min_value=0.0)

from_currency = st.selectbox("From currency", available_currencies)
to_currency = st.selectbox("To currency", available_currencies)

if st.button("Get Latest Rate"):
    latest_date = date.today()
    rate_date, conversion_rate = get_latest_rates(from_currency, to_currency, amount)  
    
    if conversion_rate:
        converted_amount = amount * conversion_rate
        inverse_rate = reverse_rate(conversion_rate) 
        rounded_conversion_rate = round_rate(conversion_rate)  
        st.write(f"Conversion Rate on {rate_date} from {from_currency} to {to_currency} was {rounded_conversion_rate}")
        st.write(f"So, {format_currency(amount, from_currency)} equals {format_currency(converted_amount, to_currency)}")
        st.write(f"The inverse rate is {round_rate(inverse_rate)}")
    else:
        st.write("Failed to fetch the latest conversion rate.")


selected_date = st.date_input("Select a date for historical conversion", value=None)
if st.button("Convert"):
    conversion_rate = get_historical_rate(from_currency, to_currency, selected_date, amount)  
    
    if conversion_rate:
        converted_amount = amount * conversion_rate
        inverse_rate = reverse_rate(conversion_rate)  
        rounded_conversion_rate = round_rate(conversion_rate)  
        st.write(f"Conversion Rate on {selected_date} from {from_currency} to {to_currency} was {rounded_conversion_rate}")
        st.write(f"So, {format_currency(amount, from_currency)} equals {format_currency(converted_amount, to_currency)}")
        st.write(f"The inverse rate is {round_rate(inverse_rate)}")
    else:
        st.write("Failed to fetch conversion rate for the selected date.")
