import s_functions
from constants import *
from read_csv import *
import random
import numpy as np


balance = [100]*100


def S_total_random():
    value = random.choice([-1, 0, 1])
    return value


def SimulationOfAlgorithm(balance,thresholdDate):
    for dateNum in range(thresholdDate,len(Dates) - 2):

        for tickerNum in range(thresholdDate,len(Tickers) - 1):

            S_function = S_total_random()
            
            if(S_function == 0):
                continue
            
            futureDay = dateNum + 1
            currentDay = dateNum

            futurePrice = get_price(df_prices,Tickers[tickerNum],Dates[futureDay])
            currentPrice = get_price(df_prices,Tickers[tickerNum],Dates[currentDay])

            if(futurePrice is None or currentPrice is None):
                continue

            if(S_function == 1):

                percentage_change = (futurePrice - currentPrice)/currentPrice
                balance[tickerNum] = balance[tickerNum] + balance[tickerNum] * percentage_change

            elif (S_function == -1):

                percentage_change =   (currentPrice - futurePrice)/currentPrice
                balance[tickerNum] = balance[tickerNum] + balance[tickerNum] * percentage_change  
    return balance              

print(np.sum(SimulationOfAlgorithm(balance,57)))



    