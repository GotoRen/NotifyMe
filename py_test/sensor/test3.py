# 人に反応してLEDライトが点灯する
# 撮影してLINE通知する
# ベータ版（テスト用）

import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import subprocess
import requests
import urllib.request as req
import json, subprocess

# LINE Notify トークン - 以下を書き換えて利用します★
TOKEN = 'S6xW5T8mU6tL6eTwSCaiFfPncnd2S4Ws5IqZYXhlVo9'
API = 'https://notify-api.line.me/api/notify'

# GPIOポートの設定
SENSOR_PORT = 23
LED_PORT = 4
PE_PORT = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PE_PORT,GPIO.OUT)
GPIO.setup(SENSOR_PORT, GPIO.IN)
GPIO.setup(LED_PORT, GPIO.OUT)

# コマンドの実行
def exec(cmd):
	r = subprocess.check_output(cmd, shell=True)
	return r.decode("utf-8").strip()

# 写真の撮影コマンドを実行(ファイル名を日時に)
last_post = datetime(2000, 1, 1) # 適当に初期化
def take_photo():
		global last_post
        # 写真を撮影
		now = datetime.now()
		fname = now.strftime('%Y-%m-%d_%H-%M-%S') + ".jpg"
		exec("fswebcam -r 1280x720 -D 5 -F 1 -S 20 /home/pi/Img/" +fname)
		# LINEに通知
        # ただし10分は通知しない
		sec = (now - last_post).seconds
		# if sec < 10 * 60: return
		if sec < 1 * 15: return
		last_post = now	
		# 通知をLINEに挿入
		post_data = {'message': '侵入者アリ'}
		headers= {'Authorization': 'Bearer ' + TOKEN}	
		files={'imageFile': open("/home/pi/Img/" +fname, 'rb')}
		res = requests.post(API, data=post_data,
            headers=headers,files=files)
		print(res.text)

# ブザーを鳴らす
def beep():
		pwm = GPIO.PWM(PE_PORT,330)
		pwm.start(50)
		sleep(0.1)
		pwm.ChangeFrequency(440)
		sleep(0.1)
		pwm.stop()

try: 
	sw = 0 # 連続撮影防止
    # 繰り返しセンサーの値を得る
	while True:
		v = GPIO.input(SENSOR_PORT)
		if v == 1:
			GPIO.output(LED_PORT, GPIO.HIGH)
			beep()
			take_photo()
			s = "侵入者あり"
			print(s)
			sw = 1
			sleep(7)
		else:
			GPIO.output(LED_PORT, GPIO.LOW)
			sw = 0
except KeyboardInterrupt:
		pass
GPIO.cleanup()







