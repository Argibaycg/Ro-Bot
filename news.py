import requests

def get_news(filter):
	response = requests.get(f'https://api.jornalia.net/api/v1/articles?apiKey={newsAPI}&search={filter}')
	print(response.json())
	response = response.json()
	article = response['articles'][0]['sourceUrl']
	return(article)