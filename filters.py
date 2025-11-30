import numpy as np

def sma(x, window):
    x = np.asarray(x, dtype=float)
    sma_values = np.zeros_like(x)

    for i in range(len(x)):
        if i < window - 1:
            sma_values[i] = np.nan
        else:
            sma_values[i] = x[i-window+1:i+1].mean()

    return sma_values


def ewma(x, lam):
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)
    y[0] = x[0]
    for n in range(1, len(x)):
        y[n] = (1 - lam) * x[n] + lam * y[n-1]
    return y

def dewma(x, lam):
    y = ewma(x, lam)
    b = ewma(y, lam)
    return b


def sma_vec(x, window):
    x = np.asarray(x, dtype=float)
    w = np.ones(window) / window
    sma = np.convolve(x, w, mode='valid')
    return sma


def ewma_vec(x, lam):
    x = np.asarray(x, dtype=float)
    n = len(x)

    weights = (1 - lam) * lam ** np.arange(n)
    y = np.convolve(x, weights[::-1], mode='full')[:n]

    return y

def dewma_vec(x, lam):
    y = ewma_vec(x, lam)
    b = ewma_vec(y, lam)
    return b

