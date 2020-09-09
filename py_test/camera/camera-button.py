import RPi.GPIO as GPIO
from time import sleep, time
from datetime import datetime
import subprocess

# GPIOポートの設定
LED_PORT = 4
PE_PORT = 18
SWITCH_PORT = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PORT, GPIO.OUT)
GPIO.setup(PE_PORT, GPIO.OUT)
GPIO.setup(SWITCH_PORT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# コマンドの実行
def exec(cmd):
	r = subprocess.check_output(cmd, shell=True)
	return r.decode("utf-8").strip()

# 写真の撮影コマンドを実行
def take_photo():
	now = datetime.now()
	f = now.strftime('%Y-%m-%d_%H-%M-%S') + ".jpg"
	exec("fswebcam -r 1280x720 -F 1 -S 20 /home/pi/Img/" +f)

# ブザーを鳴らす
def beep():
	pwm = GPIO.PWM(PE_PORT, 330)
	pwm.start(50)
	sleep(0.1)
	pwm.ChangeFrequency(440)
	sleep(0.1)
	pwm.stop()

# ボタンを押した時の動作
try:
	sw = 0
	while True:
		if GPIO.input(SWITCH_PORT) == GPIO.HIGH:
			if sw != 0: continue # 連続押し防止
			sw = 1
			GPIO.output(LED_PORT, GPIO.HIGH)
			beep()
			take_photo()
			continue
		else:
			sw = 0
			GPIO.output(LED_PORT, GPIO.LOW)
		sleep(0.1)
except KeyboardInterrupt:
	pass
GPIO.cleanup()






















	

