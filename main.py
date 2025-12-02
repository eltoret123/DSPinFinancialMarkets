import s_functions
from constants import *
from read_csv import *
import simulation
import numpy as np

balance = [100]*100

for date in Dates:
    print(date)
    print(get_price(df_prices,"AAPL",date))