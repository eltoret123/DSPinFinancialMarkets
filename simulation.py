from s_functions import*
from constants import *
from read_csv import *
from index import *
from filters import*
import random
import numpy as np


balance = [100]*100


def S_total_random():
    value = random.choice([-1, 0, 1])
    return value




def SimulationOfAlgorithm(balance, thresholdDate, filter_func, weights):
    lam = 0.0
    if filter_func == ewma:
        lam = LAMBDA_PRICE_FILTER
    elif filter_func == dewma:
        lam = LAMBDA_DEWMA_FILTER

    for tickerNum in range(len(Tickers)):
        s = []
        price = [get_price(df_prices, Tickers[tickerNum], d) for d in Dates]
        price = np.asarray(price, dtype=float)

        filt = filter_func(price, lam)
        rsi_all = rsi(price, filter_func)
        macd_line, macd_signal = macd(price, filter_func)
        stoch_k, stoch_d = stoch(price, filter_func)
        #print(rsi_all[:20])
        #print(stoch_k[:20])
        #print(stoch_d[:20])
        #print(macd_line[:20])


        for n in range(thresholdDate, len(Dates) - 1):
            futurePrice = price[n+1]
            currentPrice = price[n]

            if np.isnan(currentPrice) or np.isnan(futurePrice):
                continue
            
            if np.isnan(filt[n]) or np.isnan(rsi_all[n]) or np.isnan(macd_line[n]) or np.isnan(macd_signal[n]):
                continue

            S_sig = S_total(
                n,
                price,
                filt,
                rsi_all,
                macd_line,
                macd_signal,
                stoch_k,
                stoch_d,
                weights
            )
            
            s.append(S_sig)

            if S_sig == 0:
                continue

            pct_change = (futurePrice - currentPrice) / currentPrice
            if S_sig == 1:
                balance[tickerNum] *= (1 + pct_change)
            elif S_sig == -1:
                balance[tickerNum] *= (1 - pct_change)
        print(s)
    return balance
   

print(np.sum(SimulationOfAlgorithm(balance,40,dewma, weights_5)))

    