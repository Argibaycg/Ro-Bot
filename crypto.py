import requests
	
async def get_crypto_value(message):	
	if message.content.startswith('-bitcoin'):
		response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
		response = response.json()
		print(response)
		price = response['bitcoin']['usd']
		await message.channel.send(f'El bitcoin esta ${price} USD')

	if message.content.startswith('-eth'):
		response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
		response = response.json()
		print(response)
		price = response['ethereum']['usd']
		await message.channel.send(f'El ethereum esta ${price} USD')

	if message.content.startswith('-ada'):
		response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd')
		response = response.json()
		print(response)
		price = response[['cardano']['usd']]
		await message.channel.send(f'Cardano esta ${price} USD')

	if message.content.startswith('-shiba'):
		response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=shiba-inu&vs_currencies=usd')
		response = response.json()
		print(response)
		price = response['shiba-inu']['usd']
		await message.channel.send(f'Nuestra salvacion esta ${price:8f} USD')	