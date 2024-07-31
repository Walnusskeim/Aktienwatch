'''
Script, that shows the stock price of a company in the command line
31.07.2024
❤
'''


##################################################
#                    Imports                     #
##################################################

import yfinance as yf
import time


##################################################
#                     Code                       #
##################################################


# Replace the company name with the one you want to track.
company = "MSFT"

# Get the short name of the company
company = yf.Ticker(company)
company_name = company.info['shortName']

# Print the name of the company
print(f"Tracking {company_name} stock price...")

# Show the stock price
while True:
    data = company.history(period="1d")

    # Get the current price
    current_price = data['Close'][0]

    # Round the price to 2 decimal places
    current_price = round(current_price, 2)

    # Print the price
    print(f'{time.ctime()} {company_name}: {current_price}')

    # Wait for 10 seconds
    time.sleep(10)

