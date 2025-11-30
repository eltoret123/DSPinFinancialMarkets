from read_csv import*

csv_path = r"DSPinFinancialMarkets\PriceOfSharesTop100.csv"
df_prices = load_prices(csv_path)

ticker = "NVDA"
date = "20/08/2025"
price = get_price(df_prices, ticker, date)

print("Price:", price)
print("Tickers:", get_all_tickers(df_prices))
print("Dates:", get_all_dates(df_prices))