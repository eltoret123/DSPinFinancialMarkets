import numpy as np 

def rsi(price, filter_func, *f_args, **f_kwargs):
    price = np.asarray(price, dtype=float)

    diff = np.diff(price, prepend=price[0])

    up = np.where(diff > 0, diff, 0.0)
    down = np.where(diff < 0, -diff, 0.0)

    up_f = filter_func(up, *f_args, **f_kwargs)
    down_f = filter_func(down, *f_args, **f_kwargs)

    rs = up_f / (down_f + 1e-12)
    rsi = 1.0 - 1.0 / (1.0 + rs)

    return rsi

def macd(
    price,
    fast_filter, slow_filter, signal_filter,
    fast_args=(), fast_kwargs=None,
    slow_args=(), slow_kwargs=None,
    signal_args=(), signal_kwargs=None
):
    price = np.asarray(price, dtype=float)

    if fast_kwargs is None:
        fast_kwargs = {}
    if slow_kwargs is None:
        slow_kwargs = {}
    if signal_kwargs is None:
        signal_kwargs = {}

    fast_line = fast_filter(price, *fast_args, **fast_kwargs)
    slow_line = slow_filter(price, *slow_args, **slow_kwargs)

    macd_line = fast_line - slow_line
    signal_line = signal_filter(macd_line, *signal_args, **signal_kwargs)
    hist_line = macd_line - signal_line

    return macd_line, signal_line, hist_line

def stoch(
    price,
    window,
    k_filter=None,
    d_filter=None,
    k_args=(), k_kwargs=None,
    d_args=(), d_kwargs=None
):
    price = np.asarray(price, dtype=float)
    n = len(price)

    k_raw = np.full(n, np.nan)
    for i in range(window - 1, n):
        window_slice = price[i-window+1:i+1]
        low = window_slice.min()
        high = window_slice.max()
        if high > low:
            k_raw[i] = 100.0 * (price[i] - low) / (high - low)
        else:
            k_raw[i] = 0.0

    if k_kwargs is None:
        k_kwargs = {}
    if d_kwargs is None:
        d_kwargs = {}

    if k_filter is not None:
        k_line = k_filter(k_raw, *k_args, **k_kwargs)
    else:
        k_line = k_raw

    if d_filter is not None:
        d_line = d_filter(k_line, *d_args, **d_kwargs)
    else:
        d_line = None

    return k_line, d_line


