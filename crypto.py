import requests
	
def get_crypto_value(message):

	crypto_dic = {
		"btc" : "bitcoin",
		"ada" : "cardano",
		"eth" : "ethereum",
		"shiba" : "shiba-inu"
	}
	
	crypto_id = crypto_dic.get(message)
	response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd')
	response = response.json()
	print(response)
	price = response[crypto_id]['usd']
	if crypto_id == "shiba-inu":
		return f'${crypto_id} esta ${price:8f} USD'

	return f'{crypto_id} esta ${price} USD'