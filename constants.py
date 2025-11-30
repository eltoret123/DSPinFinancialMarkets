from read_csv import*

csv_path = r"DSPinFinancialMarkets\PriceOfSharesTop100.csv"
df_prices = load_prices(csv_path)

Tickers = get_all_tickers(df_prices)
Dates = get_all_dates(df_prices)


