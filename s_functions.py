import numpy as np
from constants import*

def discrete_signal(value, upper, lower):
    if value > upper:
        return 1
    elif value < lower:
        return -1
    else:
        return 0

def S_MACD(n, macd, macd_signal, thresh=0.0):
    if np.isnan(macd[n]) or np.isnan(macd_signal[n]):
        return 0
    value = macd[n] - macd_signal[n]
    return discrete_signal(value, thresh, -thresh)

def S_RSI(n, rsi):
    if n >= len(rsi) or np.isnan(rsi[n]):
        return 0
    if rsi[n] < RSI_LOW:
        return 1
    elif rsi[n] > RSI_HIGH:
        return -1
    else:
        return 0

def S_DIFF(n, price, filt, thresh=0.0):
    if np.isnan(price[n]) or np.isnan(filt[n]):
        return 0
    value = price[n] - filt[n]
    return discrete_signal(value, thresh, -thresh)


def S_STOCH(n, k_line, d_line, low=STOCH_LOW, high=STOCH_HIGH):
    if n == 0:
        return 0
    K_prev, D_prev = k_line[n-1], d_line[n-1]
    K_curr, D_curr = k_line[n],   d_line[n]
    if np.isnan(K_prev) or np.isnan(D_prev) or np.isnan(K_curr) or np.isnan(D_curr):
        return 0

    crossed_up = (K_prev <= D_prev) and (K_curr > D_curr)
    crossed_down = (K_prev >= D_prev) and (K_curr < D_curr)

    if crossed_up and K_curr < low:
        return 1
    if crossed_down and K_curr > high:
        return -1
    return 0
    
def S_MOMENTUM(n, price, k=10, thresh=0.0):
    if n < k or np.isnan(price[n]) or np.isnan(price[n-k]):
        return 0
    value = price[n] - price[n-k]
    return discrete_signal(value, thresh, -thresh)

    
def S_continuous(s_values, weights):
    total = 0.0
    w_sum = 0.0

    for name, s_val in s_values.items():
        if name in weights:
            w = weights[name]
            total += w * s_val
            w_sum += abs(w)

    if w_sum == 0:
        return 0.0

    return total / w_sum

def S_total(
    n,
    price,
    filt,
    rsi,
    macd,
    macd_signal,
    stoch_k_line,
    stoch_d_line,
    weights,
    mom_k=10,
    score_threshold=0.05
):
    s_values = {}

    if weights["diff"] != 0.0 :
        s_values["diff"] = S_DIFF(n, price, filt)
    if weights["rsi"] != 0.0 and n >= RSI_WINDOW:
        s_values["rsi"] = S_RSI(n, rsi)
    if weights["macd"] != 0.0 :
        s_values["macd"] = S_MACD(n, macd, macd_signal)
    if weights["stoch"] != 0.0 :
        s_values["stoch"] = S_STOCH(n, stoch_k_line, stoch_d_line)
    if weights["moment"] != 0.0 and n >= mom_k :
        s_values["moment"] = S_MOMENTUM(n, price, k=mom_k)

    total = 0.0
    w_sum = 0.0

    for name, s_val in s_values.items():
        #print(s_val)
        if name in weights:
            w = weights[name]
            total += w * s_val
            w_sum += abs(w)

    if w_sum == 0:
        score = 0.0
    else:
        score = total / w_sum

    signal = discrete_signal(score, score_threshold, -score_threshold)

    return signal



