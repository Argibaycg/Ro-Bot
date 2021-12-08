import requests

def get_meme():
	response = requests.get('https://api.imgflip.com/get_memes')
	print(response.json())
	response = response.json()
	meme = response['data']['memes'][4]['url']
	return(meme)