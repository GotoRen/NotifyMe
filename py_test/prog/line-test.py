import requests
import sys
import urllib.parse as parse

# LINE Notify トークン - 以下を書き換えて利用します★
TOKEN = 'hogehoge'
API = 'https://notify-api.line.me/api/notify'

# LINE Notifyにデータをポスト
post_data = {'message': sys.argv[1]}
headers = {'Authorization': 'Bearer ' + TOKEN}
res = requests.post(API, data=post_data, headers=headers)
print(res.text)
