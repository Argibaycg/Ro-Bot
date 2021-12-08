import discord
import os
from keep_alive import keep_alive
from crypto import get_crypto_value
from news import get_news
from meme import get_meme

newsAPI = os.environ['NEWSAPIKEY']

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('-'):
		message_bot = 'No te entendi'
		if message.content.startswith('-$'):
			message_bot = get_crypto_value(message.content[2:])
		elif  message.content.startswith('-meme'):
			message_bot = get_meme()
		elif  message.content.startswith('-noticia'):
			message_bot = message.content.split('-noticia ', 1)[1]
			message_bot = get_news(message_bot)
		elif  message.content.startswith('-falopa'):
			message_bot = 'Ahhhhh otra vez estoy tomando falopa'
		elif  message.content.startswith('-me encanta'):
			message_bot ='maldita falopa'
	await message.channel.send(message_bot)

keep_alive()
client.run(os.getenv('BOT_TOKEN'))