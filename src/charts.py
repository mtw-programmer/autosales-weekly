import matplotlib.pyplot as plt
import os

IMAGES_DIR = "reports/images"
os.makedirs(IMAGES_DIR, exist_ok=True)

def revenue_trend_chart(daily_df, filename="revenue_trend.png"):
    path = os.path.join(IMAGES_DIR, filename)
    plt.figure(figsize=(10,5))
    plt.plot(daily_df["date"], daily_df["revenue"], marker='o')
    plt.title("Daily Revenue")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return f"images/{filename}"

def top_products_chart(top_df, filename="top_products.png"):
    path = os.path.join(IMAGES_DIR, filename)
    plt.figure(figsize=(10,5))
    plt.bar(top_df["product_name"], top_df["revenue"])
    plt.title("Top Products by Revenue")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return f"images/{filename}"
