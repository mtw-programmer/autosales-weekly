from datetime import datetime
from src.load_data import load_sales_data
from src.analysis import sales_summary, top_products, daily_sales
from src.charts import revenue_trend_chart, top_products_chart
from src.report import render_html_report, html_to_pdf
from src.config import REPORT_TITLE, CURRENCY

DATA_PATH = "data/sample_sales.csv"
HTML_REPORT = "reports/weekly_report.html"
PDF_REPORT = "reports/weekly_report.pdf"

def main():
    df = load_sales_data(DATA_PATH)

    summary = sales_summary(df)
    top_df = top_products(df)
    daily_df = daily_sales(df)

    top_chart_path = top_products_chart(top_df)
    trend_chart_path = revenue_trend_chart(daily_df)

    context = {
        "title": REPORT_TITLE,
        "currency": CURRENCY,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "summary": summary,
        "top_products_chart": top_chart_path,
        "revenue_trend_chart": trend_chart_path,
    }

    render_html_report(context, HTML_REPORT)
    html_to_pdf(HTML_REPORT, PDF_REPORT)

    print("Report generated:", PDF_REPORT)

if __name__ == "__main__":
    main()
