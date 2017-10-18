import requests
import json
from pprint import pprint
import os
import time

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
r = requests.get(url, headers={'Accept': 'application/json'})
data = r.json()
curr_price = data["bpi"]["USD"]["rate_float"]
pprint(curr_price)
if curr_price > 1000000:
    os.system('say "your rich beotch"')
else:
    os.system('say "current bitcoin price is {} dollars"'.format(int(curr_price)))

