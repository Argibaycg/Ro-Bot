import discord
import os
import requests
import random
from replit import db
from keep_alive import keep_alive
newsAPI = os.environ['NEWSAPIKEY']

client = discord.Client()

def get_meme():
	response = requests.get('https://api.imgflip.com/get_memes')
	print(response.json())
	response = response.json()
	meme = response['data']['memes'][4]['url']
	return(meme)


def get_news(filter):
	response = requests.get(f'https://api.jornalia.net/api/v1/articles?apiKey={newsAPI}&search={filter}')
	print(response.json())
	response = response.json()
	article = response['articles'][0]['sourceUrl']
	return(article)

def update_phrase(phrase):
	if 'phrases' in db.keys():
		phrases = db['phrases']
		phrases.append(phrase)
		db['phrases'] = phrases
	else:
		db['phrases'] = [phrase]

def delete_phrase(index):
	phrases = db['phrases']
	if len(phrases) > index:
		del phrases[index]
		db['phrases'] = phrases

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	msg = message.content

	if message.content.startswith('-meme'):
		meme = get_meme()
		await message.channel.send(meme)

	if message.content.startswith('-noticia'):
		article = message.content.split('-noticia ', 1)[1]
		article = get_news(article)
		await message.channel.send(article)

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
		price = response['cardano']['usd']
		await message.channel.send(f'Cardano esta ${price} USD')

	if message.content.startswith('-shiba'):
		response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=shiba-inu&vs_currencies=usd')
		response = response.json()
		print(response)
		price = response['shiba-inu']['usd']
		await message.channel.send(f'Nuestra salvacion esta ${price:8f} USD')			

	if message.content.startswith('-frase'):
		if 'phrases' in db.keys():
			response_phrases = db['phrases']
			await message.channel.send(random.choice(response_phrases))

	if message.content.startswith('-falopa'):
		if 'phrases' in db.keys():
			response_phrases = db['phrases']
			await message.channel.send('Ahhhhh otra vez estoy tomando falopa')		

	if message.content.startswith('-me encanta'):
		if 'phrases' in db.keys():
			response_phrases = db['phrases']
			await message.channel.send('maldita falopa')			
		
	if message.content.startswith('-add-frase'):
		phrase = message.content.split('-add-frase ', 1)[1]
		update_phrase(phrase)
		await message.channel.send('Se agrego la frase!')

	if message.content.startswith('-del-frase'):
		phrases = []
		if 'phrases' in db.keys():
			index = message.content.split('-del-frase ', 1)[1]
			delete_phrase(index)
			phrases = db['phrases']
		await message.channel.send(phrases)


keep_alive()
client.run(os.getenv('BOT_TOKEN'))