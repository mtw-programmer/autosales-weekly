Python script, that automatically creates weekly reports from csv.


This is a personal project to practice automating e-commerce reports with Python. Not a production-ready tool.

## Setup

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```sh
python main.py
```

## CSV structure

order_id,date,product_name,quantity,price

## Report content

Generation date, Orders count, Total revenue, Avg order value, Top products chart, Daily revenue chart
