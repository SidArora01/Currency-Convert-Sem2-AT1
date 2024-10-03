# Currency Converter Using Python #
# COIN SWAP #


## Author
<h3>Name: Siddharth Arora<br>
Student ID: 25106954</h3>

## Description

**CoinSwap** is a web-application that was designed to make currency conversion easy and quick. It serves a variety of use cases, from casual purposes like assisting travelers and shoppers, to more business-oriented needs, such as supporting international traders and financial planners.

### Features
- Interactive and Easy to use User Interface (UI) through dropdown menus
- Application offers a wide range of over 30 currencies for conversion for the day
- For traders and business use case, the application offers historical conversions and inverse rates where users can select past dates and check rates.
- The rates are fetched from a credible source (European Central Bank) through Frankfurter API thus ensuring data accuracy
- Data is refreshed everyday at 1600 CET (12 AM AEST (Syd)) 

### Challenges
- Integration of external APIs and error handling
- Integrating raw data into the application to display a more user friendly output
- Frankfurter being an open source API can lead to a lack of technical support and potential compatibility issues in the future

### Future Features
- More information in the form of trend visualisations
- Realtime data updates for an extremely accurate conversion
- A profile based system where users can save and bookmark their favourite currecies 
- More diverse currency options to accomodate a wider user base


## How to Setup
**To begin this project follow the given steps:**

1. Create a virtual environment(venv) to make sure there is no dependency clash with other projects.
2. Install necessary packages and python libraries (streamlit, json, api).
3. Ideate and design a project structure.
4. Start in the venv

**Python Version**:  
- Python 3.12.3

**Required Packages**:
- streamlit == 1.36.0
- requests == 2.31.0
- api == 0.0.7
- json == 0.9.25

## How to Run the Program
1. After the program is set up in the environment go to the terminal
2. In the terminal execute the following command: streamlit run app.py

## Project Structure

├── app.py                # Main application script
├── api.py                # API interaction handler
├── frankfurter.py         # Functions for working with Frankfurter API
├── currency.py           # Helper functions for formatting currencies
├── requirements.txt      # List of required packages
└── README.md             # Project documentation

### File Description

1. **app.py** - 
2. **api.py** -
3. **frankfurter.py** -
4. **currency.py** -
