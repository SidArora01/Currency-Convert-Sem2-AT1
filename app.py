import streamlit as st
from api import get_conversion_rate, get_currency_codes
from currency import format_currency
from datetime import date

# Fetch available currencies on app start
available_currencies = get_currency_codes()

# UI elementsstreamlit run
UTS_logo = "3016.png"
st.image(image=UTS_logo)

st.title("Currency Converter")
st.subheader("BY: Siddharth Arora (25106954)")



# Input for the amount
amount = st.number_input("Enter the amount to convert", min_value=0.0)

# Dropdowns for currency selection
from_currency = st.selectbox("From currency", available_currencies)
to_currency = st.selectbox("To currency", available_currencies)


if st.button("Get Latest Rate"):
    # Get today's date
    latest_date = date.today()
    # Call the get_conversion_rate function with the latest date
    conversion_rate = get_conversion_rate(from_currency, to_currency, date=latest_date)
    converted_amount = amount * conversion_rate
    inverse_rate = 1 / conversion_rate
    st.write(f"Conversion Rate on {latest_date} from {from_currency} to {to_currency} was {conversion_rate}")
    st.write(f" So {amount} in {from_currency} corresponds to {converted_amount} in {to_currency}")
    st.write(f" The inverse rate is {inverse_rate}")
    
# Date input for historical conversion
selected_date = st.date_input("Select a date (optional)", value=None)

# Button to fetch conversion rate
if st.button("Convert"):
    conversion_rate = get_conversion_rate(from_currency, to_currency, selected_date)
    if conversion_rate:
        converted_amount = amount * conversion_rate
        st.write(f"Conversion rate: {conversion_rate}")
        st.write(f"Converted amount: {format_currency(converted_amount, to_currency)}")
    else:
        st.write("Failed to fetch conversion rate.")
