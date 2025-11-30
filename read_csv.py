import pandas as pd

def load_prices(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path, sep=";", engine="python")
    df.rename(columns={df.columns[0]: "Ticker"}, inplace=True)
    for col in df.columns[1:]:
        s = (
            df[col]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", ".", regex=False)
            .str.strip()
        )
        df[col] = pd.to_numeric(s, errors="coerce")
    return df

def get_price(df: pd.DataFrame, ticker: str, date: str):
    if ticker not in df["Ticker"].values:
        return None
    if date not in df.columns:
        return None
    price = df.loc[df["Ticker"] == ticker, date].values[0]
    if pd.isna(price):
        return None
    return float(price)

def get_all_tickers(df: pd.DataFrame):
    return df["Ticker"].tolist()

def get_all_dates(df: pd.DataFrame):
    return df.columns[1:].tolist()


