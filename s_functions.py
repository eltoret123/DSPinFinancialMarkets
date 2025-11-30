def discrete_signal(value, upper, lower):
    if value > upper:
        return 1
    elif value < lower:
        return -1
    else:
        return 0

def S1_trend(n, lead, lag, band):
    return discrete_signal(lead(n), (1 + band) * lag[n], (1 - band) * lag[n])

def S2_rsi_type1(n, lead, lag, rsi, band, rsi_l = 0.3, rsi_h = 0.7):
    s = S1_trend(n, lead, lag, band)
    if rsi[n] < rsi_l or rsi[n] > rsi_h:
        return 0
    return s

def S3_rsi_type2(n, lead, lag, rsi, band, rsi_l = 0.3, rsi_h = 0.7):
    if rsi[n] < rsi_l:
        return 1
    if rsi[n] > rsi_h:
        return -1
    return S1_trend(n, lead, lag, band)

def S_RSI(n, rsi, low=0.3, high=0.7):
    if rsi[n] < low:
        return 1
    elif rsi[n] > high:
        return -1
    else:
        return 0

def S_DIFF(n, price, filt, thresh=0.0):
    value = price[n] - filt[n]
    return discrete_signal(value, thresh, -thresh)


def S_MACD(n, macd, macd_signal, thresh=0.0):
    value = macd[n] - macd_signal[n]
    return discrete_signal(value, thresh, -thresh)

def S_STOCH(n, stoch, low=20, high=80):
    if stoch[n] < low:
        return 1
    elif stoch[n] > high:
        return -1
    else:
        return 0
    
def S_MOMENTUM(n, price, k=10, thresh=0.0):
    if n < k:
        return 0
    value = price[n] - price[n-k]
    return discrete_signal(value, thresh, -thresh)

def S_RSI_Wilder(n, rsi, rsi_l = 30, rsi_h = 70):
    if rsi[n] < rsi_l:
        return 1
    elif rsi[n] > rsi_h:
        return -1
    else:
        return 0
    
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

def S_discrete(score, threshold=0.1):
    if score > threshold:
        return 1
    elif score < -threshold:
        return -1
    else:
        return 0

def S_total(
    n,
    price,
    filt,
    rsi,
    macd,
    macd_signal,
    stoch,
    weights,
    use_diff=True,
    use_rsi=True,
    use_macd=True,
    use_stoch=True,
    use_mom=True,
    mom_k=10,
    score_threshold=0.1
):
    s_values = {}

    if use_diff:
        s_values["diff"] = S_DIFF(n, price, filt)
    if use_rsi:
        s_values["rsi"] = S_RSI(n, rsi)
    if use_macd:
        s_values["macd"] = S_MACD(n, macd, macd_signal)
    if use_stoch:
        s_values["stoch"] = S_STOCH(n, stoch)
    if use_mom:
        s_values["moment"] = S_MOMENTUM(n, price, k=mom_k)

    total = 0.0
    w_sum = 0.0

    for name, s_val in s_values.items():
        if name in weights:
            w = weights[name]
            total += w * s_val
            w_sum += abs(w)

    if w_sum == 0:
        score = 0.0
    else:
        score = total / w_sum

    signal = discrete_signal(score, score_threshold, -score_threshold)

    return score, signal



