from dotenv import load_dotenv
import requests, os
load_dotenv()

key = os.environ.get('API_KEY')


parameters = {
        'key': key,
        'q': "paris"
    }
url = f'http://api.weatherapi.com/v1/current.json'
    

response = requests.get(url, params=parameters)
data = response.json()
print(data)
