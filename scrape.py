from coinbase.wallet.client import Client
import datetime
import csv
import sys
import time

currencies = ['XLM/USD', 'CRO/USD', 'BTC/USD', 'ETH/USD']
api_key='1234'
api_secret='12'
client = Client(api_key, api_secret)
accounts = client.get_accounts()

start_date = datetime.date(2021, 11, 27)
end_date = datetime.date.today()
delta = datetime.timedelta(days=1)
if len(sys.argv) > 1:
    if (str(sys.argv[1]) == "all"):
        start_date = datetime.date(2020, 1, 1)
    else:
        start_date = end_date - delta
    while True:

        #add time to csv
        list = []
        list.append(start_date)
        print(start_date)
        start_date += delta
        for i in currencies:
            price = client.get_spot_price(currency_paid = i, date=start_date)
            list.append(price.amount)
        with open(r'prices.csv','a') as f:
            writer = csv.writer(f,lineterminator='\n')
            writer.writerow(list)
else:
    print("Valid arguments are 'all' for everything || '*' for a daily read")
