import urllib.request as req
import subprocess

s = '侵入者あり' 
print(s)
# 読み上げ
subprocess.check_output('./jtalk.sh "' +s + '"', shell=True)
	

	
