import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import subprocess
import urllib.request as req
import json, subprocess

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
def take_photo():
		now = datetime.now()
		f = now.strftime('%Y-%m-%d_%H-%M-%S') + ".jpg"
		exec("fswebcam /home/pi/Img/" +f)
	
# ブザーを鳴らす
def beep():
		pwm = GPIO.PWM(PE_PORT,330)
		pwm.start(50)
		sleep(0.1)
		pwm.ChangeFrequency(440)
		sleep(0.1)
		pwm.stop()
try:
    # 繰り返しセンサーの値を得る
	sw = 0 # 連続撮影防止
	while True:
		v = GPIO.input(SENSOR_PORT)
		if v == GPIO.HIGH:
			GPIO.output(LED_PORT, GPIO.HIGH)
			beep()
			take_photo()
			s = "侵入者あり"
			print(s)
			exec('./jtalk.sh "' +s + '"')
			sw = 1
		else:
			GPIO.output(LED_PORT, GPIO.LOW)
			sw = 0
		sleep(5)
        
except KeyboardInterrupt:
		pass
    
GPIO.cleanup()







