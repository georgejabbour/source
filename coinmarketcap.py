import urllib2, json
from tabulate import tabulate

url = 'https://api.coinmarketcap.com/v1/ticker/?limit=25'
response = urllib2.urlopen(url)
d = json.loads(response.read())
heads = ["name", "price_usd", "percent_change_1h", "percent_change_24h", "percent_change_7d"]
name=[]
price_usd=[]
percent_change_1h=[]
percent_change_24h=[]
percent_change_7d=[]

for element in d:
    name.append(element["name"])
    price_usd.append(element["price_usd"])
    percent_change_1h.append(element["percent_change_1h"])
    percent_change_24h.append(element["percent_change_24h"])
    percent_change_7d.append(element["percent_change_7d"])

things=[name, price_usd, percent_change_1h, percent_change_24h, percent_change_7d]
stuff=map(list, zip(*things))
print tabulate(stuff, headers=heads)