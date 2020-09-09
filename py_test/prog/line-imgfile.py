import requests

# imageFileでの画像送信
def LineNotify():

	# トークンと通知の設定(APIとtokenの宣言)
	TOKEN = 'S6xW5T8mU6tL6eTwSCaiFfPncnd2S4Ws5IqZYXhlVo9' #　発行されたトークンを記載
	API = 'https://notify-api.line.me/api/notify' # このAPIにアクセスする
	headers = {'Authorization': 'Bearer ' + TOKEN}

	# メッセージ
	msg = '添付画像あり-テスト画像を送信しました'
	payload = {'message':msg}
		
	# 画像
	image = './test.jpg'
	files = {"imageFile":open(image, "rb")} # バイナリデータで画像を描画
	
	# POSTメソッド
	requests.post(API, data=payload, headers=headers, files=files)

if __name__=='__main__':
	LineNotify()
