from read_csv import*

csv_path = r"DSPinFinancialMarkets\PriceOfSharesTop100.csv"
df_prices = load_prices(csv_path)

Tickers = get_all_tickers(df_prices)
Dates = get_all_dates(df_prices)

weights_1 = {
    "diff": 0.4,
    "macd": 0.4,
    "rsi":  0.2,
    "stoch": 0.0,
    "moment": 0.0
}

weights_2 = {
    "diff": 0.0,
    "macd": 0.5,
    "stoch": 0.3,
    "rsi":   0.2,
    "moment": 0.0
}

weights_3 = {
    "diff":  0.3,
    "macd":  0.3,
    "stoch": 0.2,
    "rsi":   0.2,
    "moment": 0.0
}

weights_4 = {
    "diff":   0.4,
    "macd":   0.4,
    "moment": 0.2,
    "stoch":  0.0,
    "rsi":    0.0
}

weights_5 = {
    "diff":  0.5,
    "rsi":   0.25,
    "stoch": 0.25,
    "macd":  0.0,
    "moment": 0.0
}

weights_6 = {
    "diff":   0.25,
    "macd":   0.25,
    "rsi":    0.2,
    "stoch":  0.15,
    "moment": 0.15
}

# ============================================================
# OFFICIAL CONSTANTS FOR TECHNICAL INDICATORS
# ============================================================

# RSI (Wilder, 1978)
RSI_LOW = 0.30          # oversold threshold
RSI_HIGH = 0.70         # overbought threshold

# MACD (Appel, 1979)
MACD_FAST_N = 12        # fast EMA period
MACD_SLOW_N = 26        # slow EMA period
MACD_SIGNAL_N = 9       # signal EMA period

MACD_LAMBDA_FAST = 1 - 2 / (MACD_FAST_N + 1)      # EWMA lambda for fast line
MACD_LAMBDA_SLOW = 1 - 2 / (MACD_SLOW_N + 1)      # EWMA lambda for slow line
MACD_LAMBDA_SIGNAL = 1 - 2 / (MACD_SIGNAL_N + 1)  # EWMA lambda for signal line

# Stochastic Oscillator (George Lane)
STOCH_WINDOW = 14       # window length
STOCH_LOW = 20          # oversold threshold
STOCH_HIGH = 80         # overbought threshold

# Momentum
MOMENTUM_K = 14         # momentum lookback

# Trend Filter (Alexander filter rules)
TREND_THRESHOLD = 0.02  # 2% threshold

# Score quantization for S_total
SCORE_THRESHOLD = 0.10  # dead zone width

# EWMA: lambda from N
def lambda_from_N(N): return 1 - 2 / (N + 1)   # conversion N → lambda

# General EWMA & DEWMA lambdas
EWMA_SHORT = lambda_from_N(12)         # short-term smoothing
EWMA_MEDIUM = lambda_from_N(26)        # medium-term smoothing
EWMA_LONG = lambda_from_N(50)          # long-term smoothing

DEWMA_SHORT = (EWMA_SHORT) ** 0.5      # DEWMA short-term
DEWMA_MEDIUM = (EWMA_MEDIUM) ** 0.5    # DEWMA medium-term
DEWMA_LONG = (EWMA_LONG) ** 0.5        # DEWMA long-term

# Recommended filter lambdas
LAMBDA_PRICE_FILTER = 0.92             # recommended EWMA lambda for price filtering
LAMBDA_DEWMA_FILTER = 0.96             # recommended DEWMA lambda for price filtering

# Names used in S_total
S_NAMES = ["diff", "rsi", "macd", "stoch", "moment"]   # all S-function names


