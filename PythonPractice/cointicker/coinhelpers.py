import json, urllib2

def get_coin_ids():
	coin_ids=[]
	url = 'https://api.coinmarketcap.com/v1/ticker'
	response = urllib2.urlopen(url)
	coinmarketcap_tickers = json.loads(response.read())
	for coin in coinmarketcap_tickers:
		coin_ids.append(coin["id"])
	return sorted(coin_ids)

def get_coin_names():
	coin_names=[]
	url = 'https://api.coinmarketcap.com/v1/ticker'
	response = urllib2.urlopen(url)
	coinmarketcap_tickers = json.loads(response.read())
	for coin in coinmarketcap_tickers:
		coin_names.append(coin["name"])
	return sorted(coin_names)

coin_ids = get_coin_ids()
coin_names=get_coin_names()
print coin_names