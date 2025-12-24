import pandas as pd
from src.config import TOP_PRODUCTS_LIMIT

def sales_summary(df: pd.DataFrame) -> dict:
    return {
        "orders_count": df["order_id"].nunique(),
        "total_revenue": round(df["revenue"].sum(), 2),
        "avg_order_value": round(df.groupby("order_id")["revenue"].sum().mean(), 2),
    }

def top_products(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("product_name")
        .agg(
            quantity=("quantity", "sum"),
            revenue=("revenue", "sum"),
        )
        .sort_values("revenue", ascending=False)
        .head(TOP_PRODUCTS_LIMIT)
        .reset_index()
    )

def daily_sales(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(df["date"].dt.date)
        .agg(revenue=("revenue", "sum"))
        .reset_index()
    )
