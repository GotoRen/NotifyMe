import requests
import sys
import urllib.parse as parse

# LINE Notify トークン - 以下を書き換えて利用します★
TOKEN = 'S6xW5T8mU6tL6eTwSCaiFfPncnd2S4Ws5IqZYXhlVo9'
API = 'https://notify-api.line.me/api/notify'

# LINE Notifyにデータをポスト
post_data = {'message': sys.argv[1]}
headers = {'Authorization': 'Bearer ' + TOKEN}
res = requests.post(API, data=post_data, headers=headers)
print(res.text)
