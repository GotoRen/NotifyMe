import requests
import env_set

TOKEN = env_set.TOKEN
API = env_set.API

def LineNotify():

	headers = {'Authorization': 'Bearer ' + TOKEN}

	msg = '添付画像あり-テスト画像を送信しました'
	payload = {'message':msg}

	image = './test.jpg'
	files = {"imageFile":open(image, "rb")}
	
	requests.post(API, data=payload, headers=headers, files=files)



if __name__=='__main__':
	LineNotify()
