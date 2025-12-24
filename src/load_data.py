import pandas as pd

def load_sales_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    df["date"] = pd.to_datetime(df["date"])
    df["revenue"] = df["quantity"] * df["price"]

    return df
