import streamlit as st
from frankfurter import get_latest_rates, get_historical_rate, get_currencies_list  
from currency import  round_rate, reverse_rate, format_output
from datetime import date


available_currencies = get_currencies_list()


#UI Design
UTS_logo = "UTS-logo.jpg"
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(UTS_logo, use_column_width=True)

col1, col2, col3, col4, col5 = st.columns([1, 1,3,1, 1])
with col3:
    st.title ("CoinSwap")
    st.subheader("Currency Converter")
    st.subheader("BY: Siddharth Arora (25106954)")


#User Input
#Error Handling if no Currencies are fetched or if an empty list is there
amount = st.number_input("Enter the amount to convert", min_value=0.0)

if available_currencies is None or len(available_currencies) == 0:
    st.error("Error: Unable to fetch the list of available currencies.")
else:
    from_currency = st.selectbox("From currency", available_currencies)
    to_currency = st.selectbox("To currency", available_currencies)


#Button for Latest Rate
#Error Handling if No Conversion Rate is returned
if st.button("Get Latest Conversion Rate"):
    latest_date = date.today()
    rate_date, conversion_rate = get_latest_rates(from_currency, to_currency)  
    
    if conversion_rate:
        converted_amount = amount * conversion_rate
        inverse_rate = reverse_rate(conversion_rate) 
        rounded_conversion_rate = round_rate(conversion_rate)  
        st.write(format_output(amount= amount, date=latest_date, from_currency=from_currency, to_currency=to_currency,rate=rounded_conversion_rate, inverse_rate=inverse_rate))
    else:
        st.write("Failed to fetch the latest conversion rate.")


#Calendar Feature for Historical Date Selection, making user interaction better than just putting dates manually
#Error Handling 1. If Future Date is input, it returns appropriate string
#Error Handling 2. If No date is entered, it returns appropriate string
selected_date = st.date_input("Select a date for historical conversion", value=None)

if st.button("Get Historical Conversion Rate"):
    if selected_date is None:
        st.write("Please select a date.")
    else:
        today = date.today()
        if selected_date <= today:
            conversion_rate = get_historical_rate(from_currency, to_currency, selected_date.strftime("%Y-%m-%d"))  
            if conversion_rate:
                converted_amount = amount * conversion_rate
                inverse_rate = reverse_rate(conversion_rate)  
                rounded_conversion_rate = round_rate(conversion_rate)  
                st.write(format_output(amount=amount, date=selected_date, from_currency=from_currency, to_currency=to_currency, rate=rounded_conversion_rate, inverse_rate=inverse_rate))
            else:
                st.write("Failed to fetch conversion rate for the selected date.")
        else:
            st.write("Error: Cannot fetch rates for future dates.")

        
