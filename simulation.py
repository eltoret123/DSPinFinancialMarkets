from s_functions import*
from constants import *
from read_csv import *
import random
import numpy as np


balance = [100]*100


def S_total_random():
    value = random.choice([-1, 0, 1])
    return value


def SimulationOfAlgorithm(balance,thresholdDate, filteredPrice, weights):
    for dateNum in range(thresholdDate,len(Dates) - 1):

        for tickerNum in range(thresholdDate,len(Tickers) - 1):
            
            futureDay = dateNum + 1
            currentDay = dateNum

            futurePrice = get_price(df_prices,Tickers[tickerNum],Dates[futureDay])
            currentPrice = get_price(df_prices,Tickers[tickerNum],Dates[currentDay])
            
            RSI = rsi()
            
            S_function = S_total(dateNum, currentPrice, filteredPrice, )
            
            if(S_function == 0):
                continue
            


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



    