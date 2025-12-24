Python script, that automatically creates weekly reports from csv.

## Setup

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## CSV structure

order_id,date,product_name,quantity,price

## Report content

Generation date, Orders count, Total revenue, Avg order valueW
