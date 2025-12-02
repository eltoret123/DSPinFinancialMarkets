<<<<<<< HEAD
from read_csv import*
from constants import*

csv_path = r"DSPinFinancialMarkets\PriceOfSharesTop100.csv"
#df_prices = load_prices(csv_path)

ticker = "NVDA"
date = "9/10/2025"
price = get_price(df_prices, ticker, date)

print("Price:", price)
print("Tickers:", get_all_tickers(df_prices))
print("Dates:", get_all_dates(df_prices))

for date in Dates:
    print(get_price(df_prices, "AAPL", date))
=======
import s_functions
from constants import *
from read_csv import *
import simulation
import numpy as np

balance = [100]*100



