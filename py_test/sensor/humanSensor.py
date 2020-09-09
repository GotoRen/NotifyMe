# coding: utf-8
import RPi.GPIO as GPIO
import time
from datetime import datetime
 
GPIO.setmode(GPIO.BCM) # GPIO番号設定
GPIO.setup(23, GPIO.IN) # 入力設定
 
while True:
	nowTime = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
	# 0 -> 人の気配なし， 1 -> 人の気配あり
	print(nowTime+' ['+str(GPIO.input(23))+']')
	time.sleep(1)