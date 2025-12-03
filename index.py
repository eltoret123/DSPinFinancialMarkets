import numpy as np
from constants import*

def rsi(price, filter_func):
    price = np.asarray(price, dtype=float)

    diff = np.diff(price, prepend=price[0])

    up = np.where(diff > 0, diff, 0.0)
    down = np.where(diff < 0, -diff, 0.0)

    up_f = filter_func(up, RSI_LAMBDA)
    down_f = filter_func(down, RSI_LAMBDA)

    rs = up_f / (down_f + 1e-12)
    rsi = 1.0 - 1.0 / (1.0 + rs)

    return rsi

def macd(price, filter):
    price = np.asarray(price, dtype=float)
    
    fast_line = filter(price, MACD_LAMBDA_FAST)
    slow_line = filter(price, MACD_LAMBDA_SLOW)

    macd_line = fast_line - slow_line
    signal_line = filter(macd_line, MACD_LAMBDA_SIGNAL)
    hist_line = macd_line - signal_line

    return macd_line, signal_line

def stoch(price, d_filter=None):
    price = np.asarray(price, dtype=float)
    n = len(price)
    window = STOCH_WINDOW
    k_raw = np.full(n, np.nan)
    for i in range(window - 1, n):
        window_slice = price[i-window+1:i+1]
        low = window_slice.min()
        high = window_slice.max()
        if high > low:
            k_raw[i] = 100.0 * (price[i] - low) / (high - low)
        else:
            k_raw[i] = 0.0
    
    k_line = k_raw

    if d_filter is not None:
        d_line = d_filter(k_line, STOCH_LAMBDA)
    else:
        d_line = None

    return k_line, d_line


