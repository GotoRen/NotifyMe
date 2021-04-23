import requests
import sys
import urllib.parse as parse
import env_set

TOKEN = env_set.TOKEN
API = env_set.API

post_data = {'message': sys.argv[1]}
headers = {'Authorization': 'Bearer ' + TOKEN}
res = requests.post(API, data=post_data, headers=headers)
print(res.text)
