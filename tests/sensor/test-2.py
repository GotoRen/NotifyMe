# 人に反応してLEDライトが点灯する
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import subprocess
import requests
import urllib.request as req
import json, subprocess
import env_set

TOKEN = env_set.TOKEN
API = env_set.API

SENSOR_PORT = 23
LED_PORT = 4
PE_PORT = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PE_PORT,GPIO.OUT)
GPIO.setup(SENSOR_PORT, GPIO.IN)
GPIO.setup(LED_PORT, GPIO.OUT)

def exec(cmd):
	r = subprocess.check_output(cmd, shell=True)
	return r.decode("utf-8").strip()

last_post = datetime(2000, 1, 1)
def take_photo():
		global last_post
		now = datetime.now()
		fname = now.strftime('%Y-%m-%d_%H-%M-%S') + ".jpg"
		exec("fswebcam -r 1280x720 -F 1 -S 20 /home/pi/Img/" +fname)
		
		# 15秒間は通知しない
		sec = (now - last_post).seconds 
		if sec < 1 * 15: 
			print("通知実行")
			return
		last_post = now	

		post_data = {'message': '侵入者アリ'}
		headers= {'Authorization': 'Bearer ' + TOKEN}	
		files={'imageFile': open("/home/pi/Img/" +fname, 'rb')}
		res = requests.post(API, data=post_data, headers=headers,files=files)
		print(res.text)

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
		if v == GPIO.HIGH:
			GPIO.output(LED_PORT, GPIO.HIGH)
		else:
			GPIO.output(LED_PORT, GPIO.LOW)
			sw = 0
except KeyboardInterrupt:
		pass
GPIO.cleanup()
